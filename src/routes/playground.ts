import { Router, Request, Response } from 'express';
import { fetchADKReport } from '../lib/adkClient';

const router = Router();

// Define route handler
router.post('/playground', async (req: Request, res: Response) => {
  try {
    const topic = req.body.topic;
    
    if (req.body.use_adk) {
      try {
        const report = await fetchADKReport(topic);
        res.json({ report });
      } catch (error: any) {
        res.status(500).json({ error: error.message });
      }
      return;
    }
  
    // Existing MCP Playground logic would go here
    res.json({ 
      result: "This is the standard MCP response (not using ADK)",
      topic: topic,
      timestamp: new Date().toISOString()
    });
  } catch (error: any) {
    res.status(500).json({ error: error.message });
  }
});

export default router; 