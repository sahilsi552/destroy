from .. import db

rulesdb = db.rulesdb

async def set_rule(chat_id, rules_text):
  
    await rulesdb.update_one(
        {"chat_id": chat_id}, 
        {"$set": {"text": rules_text}}, 
        upsert=True
    )

async def get_rule(chat_id):
    # This function retrieves the current rules for a given chat
    rule_entry = await rulesdb.find_one({"chat_id": chat_id})
    rules_text = rule_entry["text"]  if rule_entry else None
    return rules_text  # Return the rules text or a default message

async def remove_rule(chat_id):
    # This function removes the current rules
    await rulesdb.delete_one({"chat_id": chat_id})
