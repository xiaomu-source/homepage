import service from '../server'

export const permissionsTree = (data) => {
    return service.post('/v1/sys/permissions/tree/', data)
}
export const permissionsList = (data) => {
    return service.post('/v1/sys/permissions/get-list/', data)
}
export const permissionsCreate = (data) => {
    return service.post('/v1/sys/permissions/create-permission/', data)
}
export const permissionsUpdate = (data) => {
    return service.post('/v1/sys/permissions/update-permission/', data)
}
export const permissionsDelete = (data) => {
    return service.post('/v1/sys/permissions/delete-permission/', data)
}
export const permissionsStop = (data) => {
    return service.post('/v1/sys/permissions/stop/', data)
}






