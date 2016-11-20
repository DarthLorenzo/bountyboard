from app import models

sort_options_dict = {
    '1': {"label": "Newest", "field": models.Bounty.created_at},
    '2': {"label": "Oldest", "field": models.Bounty.created_at.desc()},
    '3': {"label": "Biggest First", "field": models.Bounty.pledge_sum}
}

def get_bounties(offset=0, sort_option=None):
    if isinstance(sort_option, basestring):
        sort_option = sort_options_dict.get(sort_option, {}).get("field", None)
    return models.Bounty.query.order_by(sort_option).offset(offset).limit(10).all()
