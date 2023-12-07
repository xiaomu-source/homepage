# 用于开发时一键构建测试环境
if (($1 == 0))
then
  echo "移除旧的容器"
  docker rm -f homepage-nginx-1 homepage-web-1 homepage-redis-1 homepage-db-1
  echo "移除旧的镜像"
  docker image rm homepage-nginx homepage-web
  echo "移除旧的卷"
  docker volume rm homepage_static_vol homepage_media_vol homepage_redis_vol  homepage_db_vol
  echo "打包本地镜像"
  docker-compose build
  exit 0
fi
echo "启动服务。。。"
docker-compose up