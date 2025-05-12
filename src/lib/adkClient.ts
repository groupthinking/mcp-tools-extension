import axios from 'axios';
import dotenv from 'dotenv';

dotenv.config();

export async function fetchADKReport(topic: string): Promise<string> {
  const url = process.env.ADK_SERVICE_URL || "http://localhost:8000";
  try {
    const response = await axios.post(`${url}/generate_report`, { topic });
    return response.data.report;
  } catch (error: any) {
    throw new Error(`ADK service error: ${error.response?.data?.detail || error.message}`);
  }
} 