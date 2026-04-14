import React from 'react';
import { Brain, User } from 'lucide-react';
import { format } from 'date-fns';

const ChatMessage = ({ sender, message, timestamp }) => {
  const isAI = sender === 'ai';

  return (
    <div className={`flex gap-3 ${isAI ? 'flex-row' : 'flex-row-reverse'}`}>
      <div className={`flex-shrink-0 w-10 h-10 rounded-xl flex items-center justify-center ${
        isAI 
          ? 'bg-gradient-to-br from-cyan-500 to-blue-600' 
          : 'bg-gray-700'
      }`}>
        {isAI ? (
          <Brain className="w-5 h-5 text-white" />
        ) : (
          <User className="w-5 h-5 text-white" />
        )}
      </div>

      <div className={`flex-1 max-w-[80%] ${isAI ? 'items-start' : 'items-end'}`}>
        <div className={`rounded-2xl px-4 py-3 ${
          isAI 
            ? 'bg-gray-900/50 border border-gray-800' 
            : 'bg-gradient-to-r from-cyan-500 to-blue-600'
        }`}>
          <p className={`text-sm leading-relaxed ${isAI ? 'text-gray-200' : 'text-white'}`}>
            {message}
          </p>
        </div>
        {timestamp && (
          <p className="text-xs text-gray-500 mt-1 px-2">
            {format(new Date(timestamp), 'h:mm a')}
          </p>
        )}
      </div>
    </div>
  );
};

export default ChatMessage;