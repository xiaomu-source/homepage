# 用于开发时一键构建测试环境
if (($1 == 0))
then
  echo "移除旧的数据库容器"
  docker rm -f homepage-redis-1 homepage-db-1
  docker volume rm homepage_redis_vol  homepage_db_vol
  echo "移除成功, 不传参再执行一次吧"
  exit 0
fi
echo "启动 Databases 。。。"
cd .. && docker-compose up -d
echo "启动 Web 。。。"
cd ./server/server/
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 3090