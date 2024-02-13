#from flask import Flask

# app.py인 곳을 입구로 찾아서 기본적으로 실행합니다
# 또는 FLASK_APP이라는 환경변수의 이름을 파일명으로 변경합니다
# set FLASK_APP=test 
# wsgi.py에 직접 키=밸류로 여러 환경변수들을 기입합니다.
#test = Flask(__name__)

#@test.route("/")
#def hello():
    #return f'Hello {__name__}'

# localhost:500/bye 로 접속하면 bye 만 출력되도록 컨트롤러를 만들어주세요

#-----------------------------------------------------------

#from flask import Flask

#def create_app():
#     app = Flask(__name__)

     # URL과 FLASK코드를 매핑하는 Flask 데코레이터
     # @app.route처럼 애노테이션으로 URL을 매핑하는 함수를 라우팅 함수라고 부릅니다.
#     @app.route('/')
#     def hello():
#          return f'Hello, {__name__}'

#     @app.route('/yeonji')
#     def hello_yeonji():
#          return f'Hello, yeonji'
    
#     return app

#---------------------------------------------------------

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# app.py인 곳을 입구로 찾아서 기본적으로 실행합니다
# 또는 FLASK_APP이라는 환경변수의 이름을 파일명으로 변경합니다
# set FLASK_APP=test 
# wsgi.py에 직접 키=밸류로 여러 환경변수들을 기입합니다.

import config

db = SQLAlchemy()
migrate = Migrate()


## test/__init__.py
def create_app(): # 어플리케이션 팩토리 - 플라스크 서버가 실행될 때 가장 최초로 실행되는 생성자
    test = Flask(__name__)
   
    # ORM
    test.config.from_object(config)
    db.init_app(test)
    migrate.init_app(test, db)

    # 블루프린트
    from .views import main_views, board_views  # views 폴더 및의 main_views.py 임포트
    test.register_blueprint(main_views.bp)
    test.register_blueprint(board_views.board)
    
    return test