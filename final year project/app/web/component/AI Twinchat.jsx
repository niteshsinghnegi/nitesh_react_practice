import React, { useState, useEffect, useRef } from 'react';
import { useAuth } from '@/contexts/AuthContext.jsx';
import pb from '@/lib/pocketbaseClient';
import { analyzeBehavior, getContextualResponse } from '@/lib/BehaviorAnalyzer.js';
import ChatMessage from '@/components/ChatMessage.jsx';
import { Button } from '@/components/ui/button';
import { Textarea } from '@/components/ui/textarea';
import { Send, Loader2 } from 'lucide-react';
import { toast } from 'sonner';

const AITwinChat = () => {
  const { currentUser } = useAuth();
  const [messages, setMessages] = useState([]);
  const [inputMessage, setInputMessage] = useState('');
  const [loading, setLoading] = useState(false);
  const [behaviorAnalysis, setBehaviorAnalysis] = useState(null);
  const messagesEndRef = useRef(null);

  useEffect(() => {
    if (currentUser) {
      loadChatHistory();
      loadBehaviorProfile();
    }
  }, [currentUser]);

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const loadChatHistory = async () => {
    try {
      const records = await pb.collection('chat_messages').getFullList({
        filter: `userId = "${currentUser.id}"`,
        sort: 'created',
        $autoCancel: false
      });
      setMessages(records);
    } catch (error) {
      console.error('Error loading chat history:', error);
    }
  };

  const loadBehaviorProfile = async () => {
    try {
      const analysis = await analyzeBehavior(currentUser.id);
      setBehaviorAnalysis(analysis);
    } catch (error) {
      console.error('Error loading behavior profile:', error);
    }
  };

  const handleSendMessage = async (e) => {
    e.preventDefault();
    if (!inputMessage.trim() || loading) return;

    const userMessage = inputMessage.trim();
    setInputMessage('');
    setLoading(true);

    try {
      const userRecord = await pb.collection('chat_messages').create({
        userId: currentUser.id,
        sender: 'user',
        message: userMessage
      }, { $autoCancel: false });

      setMessages(prev => [...prev, userRecord]);

      await new Promise(resolve => setTimeout(resolve, 800));

      const aiResponse = behaviorAnalysis 
        ? getContextualResponse(userMessage, behaviorAnalysis)
        : "I'm still learning about you. Complete the onboarding questionnaire to help me understand you better.";

      const aiRecord = await pb.collection('chat_messages').create({
        userId: currentUser.id,
        sender: 'ai',
        message: aiResponse,
        behaviorContext: behaviorAnalysis ? JSON.stringify(behaviorAnalysis.patterns) : null
      }, { $autoCancel: false });

      setMessages(prev => [...prev, aiRecord]);
    } catch (error) {
      console.error('Error sending message:', error);
      toast.error('Failed to send message');
    } finally {
      setLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage(e);
    }
  };

  return (
    <div className="flex flex-col h-full">
      <div className="flex-1 overflow-y-auto px-4 py-6 space-y-4">
        {messages.length === 0 ? (
          <div className="flex items-center justify-center h-full">
            <div className="text-center max-w-md">
              <p className="text-gray-400 mb-4">
                Start a conversation with your digital twin
              </p>
              <p className="text-sm text-gray-500">
                Your AI twin learns from your behavior patterns to provide personalized insights
              </p>
            </div>
          </div>
        ) : (
          messages.map((msg) => (
            <ChatMessage
              key={msg.id}
              sender={msg.sender}
              message={msg.message}
              timestamp={msg.created}
            />
          ))
        )}
        <div ref={messagesEndRef} />
      </div>

      <div className="border-t border-gray-800 p-4 bg-[#0a0a0a]">
        <form onSubmit={handleSendMessage} className="flex gap-2">
          <Textarea
            value={inputMessage}
            onChange={(e) => setInputMessage(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Type your message..."
            className="bg-gray-900 border-gray-800 text-white placeholder:text-gray-500 resize-none"
            rows={1}
            disabled={loading}
          />
          <Button
            type="submit"
            disabled={!inputMessage.trim() || loading}
            className="bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-600 hover:to-blue-700 text-white px-6"
          >
            {loading ? (
              <Loader2 className="w-5 h-5 animate-spin" />
            ) : (
              <Send className="w-5 h-5" />
            )}
          </Button>
        </form>
      </div>
    </div>
  );
};

export default AITwinChat;