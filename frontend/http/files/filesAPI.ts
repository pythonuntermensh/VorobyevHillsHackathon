import axios, { AxiosResponse } from "axios"

export const getFiles = async (): Promise<AxiosResponse<any>> => {
  return await axios.get("http://176.109.106.55:8000/files")
}

export const classifyFiles = async (formData: FormData): Promise<AxiosResponse<any>> => {
  return await axios.post("http://176.109.106.55:8000/uploads", formData)
}