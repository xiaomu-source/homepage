import service from '../server'
export const portfoliosList = (data) => {
    return service.post('/v1/blog/portfolios/get-list/', data)
}
export const portfoliosCreate = (data) => {
    return service.post('/v1/blog/portfolios/create-portfolio/', data)
}
export const portfoliosUpdate = (data) => {
    return service.post('/v1/blog/portfolios/update-portfolio/', data)
}
export const portfoliosDelete = (data) => {
    return service.post('/v1/blog/portfolios/delete-portfolio/', data)
}




