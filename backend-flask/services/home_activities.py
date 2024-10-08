from datetime import datetime, timedelta, timezone
from opentelemetry import trace
#from lib.db import pool, query_wrap_object, query_wrap_array
from lib.db import db
import logging

tracer = trace.get_tracer("home.activities")


class HomeActivities:
  def run(cognito_user_id=None):
    print("HOME ACTIVITY")
    
    # Logger.info("HomeActivities")
    #with tracer.start_as_current_span("home-activites-mock-data"):
    #  span = trace.get_current_span()
    #  now = datetime.now(timezone.utc).astimezone()
    #  span.set_attribute("app.now", now.isoformat())
    sql = db.template('activities','home')
    results = db.query_array_json(sql)
    return results