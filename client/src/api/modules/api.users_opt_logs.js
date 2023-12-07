import service from '../server'

export const users_opt_logsList = (data) => {
    return service.post('/v1/sys/users_opt_logs/get-list/', data)
}
export const users_opt_logsCreate = (data) => {
    return service.post('/v1/sys/users_opt_logs/create-log/', data)
}
export const users_opt_logsUpdate = (data) => {
    return service.post('/v1/sys/users_opt_logs/update-log/', data)
}
export const users_opt_logsDelete = (data) => {
    return service.post('/v1/sys/users_opt_logs/delete-log/', data)
}
export const users_opt_logsDeleteAll = (data) => {
    return service.post('/v1/sys/users_opt_logs/deleteAll/', data)
}
// 导出需要指定响应类型未blob
export const users_opt_logsExport = (data) => {
    return service.post('/v1/sys/users_opt_logs/export/', data,null,'blob')
}
// 导入
export const users_opt_logsImport = (data) => {
    return service.post('/v1/sys/users_opt_logs/import/', data)
}
// 导出模板
export const users_opt_logsDownloadTemplate = (data) => {
    return service.post('/v1/sys/users_opt_logs/downloadTemplate/', data,null,'blob')
}




