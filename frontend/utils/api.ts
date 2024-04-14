import axios from "axios";

interface FormattedData {
  airline_name: string;
  flight_duration: number;
  takeoff_time: number;
  class_of_service_data: ClassOfServiceData[];
  special_menu_codes: any[];
}

interface ClassOfServiceData {
  type: string;
  amount: number;
}

export const getMenu = async (body: FormattedData) => {
  try {
    return await axios.post('https://air-food.onrender.com/menu', {
      ...body
    });
  } catch (error) {
    console.error(error);
  }
}

export const getFlights = async () => {
  try {
    return await axios.get('https://air-food.onrender.com/flights');
  } catch (error) {
    console.error(error);
  }
}