import service from '../server'
export const blog_articlesList = (data) => {
    return service.post('/v1/blog/blog_articles/get-list/', data)
}
export const blog_articlesCreate = (data) => {
    return service.post('/v1/blog/blog_articles/create-blog/', data)
}
export const blog_articlesUpdate = (data) => {
    return service.post('/v1/blog/blog_articles/update-blog/', data)
}
export const blog_articlesDelete = (data) => {
    return service.post('/v1/blog/blog_articles/delete-blog/', data)
}
export const blog_articlesUploadMd = (data) => {
    return service.post('/v1/blog/blog_articles/uploadMd/', data)
}




