from sqlalchemy import create_engine, text

db_connection_string="mysql+pymysql://ez88in57ecvebktllmxj:pscale_pw_iJZaex55BzB3RzHQoeGS2uzILzRl7Y91F3ipuQeb4pQ@aws.connect.psdb.cloud/swd?charset=utf8mb4"
engine = create_engine(
  db_connection_string, 
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })

