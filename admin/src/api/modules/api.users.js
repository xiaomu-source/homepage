import service from '../server'

export const usersList = (data) => {
    return service.post('/v1/sys/users/get-list/', data)
}
export const usersCreate = (data) => {
    return service.post('/v1/sys/users/create-user/', data)
}
export const usersUpdate = (data) => {
    return service.post('/v1/sys/users/update-user/', data)
}
export const usersDelete = (data) => {
    return service.post('/v1/sys/users/delete-user/', data)
}
// 重置密码
export const usersReset = (data) => {
    return service.post('/v1/sys/users/reset/', data)
}
// 获取用户信息
export const usersFindOne = (data) => {
    return service.post('/v1/sys/users/findOne/', data)
}


