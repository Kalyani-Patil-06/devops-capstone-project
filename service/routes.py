from flask import Blueprint, jsonify, request

accounts_bp = Blueprint("accounts", __name__)
_accounts = {}
_next_id = 1


def reset_accounts():
    """Reset in-memory records; useful for tests and local demos."""
    global _accounts, _next_id
    _accounts = {}
    _next_id = 1


def _valid_payload(data, partial=False):
    if not isinstance(data, dict):
        return False
    required = ("name", "email")
    if partial:
        return any(key in data for key in required) and all(
            key in required for key in data
        )
    return all(isinstance(data.get(key), str) and data[key].strip() for key in required)


@accounts_bp.route("/accounts", methods=["POST"])
def create_account():
    global _next_id
    data = request.get_json(silent=True)
    if not _valid_payload(data):
        return jsonify({"error": "JSON body must include non-empty name and email strings"}), 400
    account = {"id": _next_id, "name": data["name"].strip(), "email": data["email"].strip()}
    _accounts[_next_id] = account
    _next_id += 1
    return jsonify(account), 201


@accounts_bp.route("/accounts", methods=["GET"])
def list_accounts():
    return jsonify([_accounts[key] for key in sorted(_accounts)]), 200


@accounts_bp.route("/accounts/<int:account_id>", methods=["GET"])
def read_account(account_id):
    account = _accounts.get(account_id)
    if account is None:
        return jsonify({"error": "Account not found"}), 404
    return jsonify(account), 200


@accounts_bp.route("/accounts/<int:account_id>", methods=["PUT"])
def update_account(account_id):
    account = _accounts.get(account_id)
    if account is None:
        return jsonify({"error": "Account not found"}), 404
    data = request.get_json(silent=True)
    if not _valid_payload(data, partial=True):
        return jsonify({"error": "JSON body must include name and/or email string fields"}), 400
    for key in ("name", "email"):
        if key in data:
            if not isinstance(data[key], str) or not data[key].strip():
                return jsonify({"error": f"{key} must be a non-empty string"}), 400
            account[key] = data[key].strip()
    return jsonify(account), 200


@accounts_bp.route("/accounts/<int:account_id>", methods=["DELETE"])
def delete_account(account_id):
    if account_id not in _accounts:
        return jsonify({"error": "Account not found"}), 404
    del _accounts[account_id]
    return "", 204
