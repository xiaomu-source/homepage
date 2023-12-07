import service from '../server'
export const resourcesList = (data) => {
    return service.post('/v1/sys/resources/get-list/', data)
}
export const resourcesCreate = (data) => {
    return service.post('/v1/sys/resources/create-resource/', data)
}
export const resourcesUpdate = (data) => {
    return service.post('/v1/sys/resources/update-resource/', data)
}
export const resourcesDelete = (data) => {
    return service.post('/v1/sys/resources/delete-resource/', data)
}




