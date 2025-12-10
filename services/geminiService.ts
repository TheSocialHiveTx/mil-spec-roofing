import { GoogleGenAI, GenerateContentResponse } from "@google/genai";

let client: GoogleGenAI | null = null;

const getClient = (): GoogleGenAI | null => {
  if (!client) {
    // Safety check: In some static environments, 'process' might not be defined.
    // We check availability to prevent a full app crash (White Screen of Death).
    let apiKey: string | undefined;
    
    try {
      apiKey = process.env.API_KEY;
    } catch (e) {
      console.warn("Environment variable access failed. AI features will be unavailable.");
    }

    if (!apiKey) {
      console.warn("Gemini API Key is missing. AI features will be disabled.");
      // Return null instead of throwing to keep the UI alive
      return null;
    }
    
    try {
      client = new GoogleGenAI({ apiKey });
    } catch (error) {
       console.error("Failed to initialize Gemini client:", error);
       return null;
    }
  }
  return client;
};

export const sendMessageToGemini = async (
  message: string, 
  history: string[]
): Promise<string> => {
  try {
    const ai = getClient();
    
    if (!ai) {
      return "Status: Offline. I cannot connect to the command center (API Key missing). Please contact HQ by phone.";
    }
    
    // Construct a context-aware prompt
    const systemInstruction = `You are "Sergeant Shingle", the AI virtual assistant for Mil-Spec Roofing. 
    Your tone is professional, authoritative yet friendly, and reliable—like a military veteran.
    You help customers with:
    1. Basic roofing questions (shingles vs metal, leak repair, storm damage).
    2. Explaining the "Mil-Spec" standard: precision, durability, integrity.
    3. Scheduling estimates (encourage them to use the contact form or call 555-0123).
    4. Do NOT give specific price quotes, but give price *ranges* for typical work if asked (e.g., "Asphalt shingles typically range from $3.50-$5.50 per sq ft depending on materials...").
    
    Keep answers concise (under 3 sentences usually) unless explaining a complex topic.`;

    const model = "gemini-2.5-flash";
    
    const chat = ai.chats.create({
      model: model,
      config: {
        systemInstruction: systemInstruction,
      }
    });
    
    const result: GenerateContentResponse = await chat.sendMessage({
      message: message
    });

    return result.text || "I copy that, but I'm having trouble processing the request. Please contact our HQ directly.";
  } catch (error) {
    console.error("Gemini API Error:", error);
    return "Negative. I cannot connect to the server right now. Please try again later or call our office.";
  }
};