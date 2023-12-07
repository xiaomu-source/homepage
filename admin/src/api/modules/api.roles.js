import service from '../server'

export const rolesList = (data) => {
    return service.post('/v1/sys/roles/get-list/', data)
}
export const rolesCreate = (data) => {
    return service.post('/v1/sys/roles/create-role/', data)
}
export const rolesUpdate = (data) => {
    return service.post('/v1/sys/roles/update-role/', data)
}
export const rolesDelete = (data) => {
    return service.post('/v1/sys/roles/delete-role/', data)
}
export const rolesFindOne = (data) => {
    return service.post('/v1/sys/roles/findOne/', data)
}

