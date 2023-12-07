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
if (($1 == 1))
then
  echo "打包前端资源"
  echo "admin 打包中..."
  cd ../admin/
  npm run build
  echo "admin 打包成功"
  echo "client 打包中..."
  cd ../client/
  npm run build
  echo "client 打包成功"
  cp -rf ./dist/ ../server/compose/nginx/client/dist/
  cp -rf ../admin/dist/ ../server/compose/nginx/admin/dist/
  cp -rf ../admin/dist/assets ../server/compose/nginx/client/dist/assets
  cd ../server/
  exit 0
if
echo "启动服务。。。"
docker-compose up