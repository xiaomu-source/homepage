import service from '../server'
export const messagesList = (data) => {
    return service.post('/v1/blog/messages/get-list/', data)
}
export const messagesCreate = (data) => {
    return service.post('/v1/blog/messages/create-message/', data)
}
export const messagesUpdate = (data) => {
    return service.post('/v1/blog/messages/update-message/', data)
}
export const messagesDelete = (data) => {
    return service.post('/v1/blog/messages/delete-message/', data)
}




export const messagesReply = (data) => {
    return service.post('/v1/blog/messages/client/reply/', data)
}
export const messagesLike = (data) => {
    return service.post('/v1/blog/messages/client/like/', data)
}
export const messagesOpposeNum = (data) => {
    return service.post('/v1/blog/messages/client/opposeNum/', data)
}
