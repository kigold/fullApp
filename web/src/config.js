const config = {
  apiBaseUrl:
    process.env.NODE_ENV === 'production'
      ? 'https://sample.herokuapp.com/api/v1'
      : 'http://localhost:8000',
  imageBaseUrl:
    process.env.NODE_ENV === 'production'
      ? 'https://sample_images'
      : 'http://localhost:2000/images',
  pageSize: 3
}

export default config
