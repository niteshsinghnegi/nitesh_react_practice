import React from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { format } from 'date-fns';

const BehaviorCard = ({ category, question, answer, timestamp }) => {
  const categoryColors = {
    daily_routines: 'text-blue-400 bg-blue-500/10 border-blue-500/20',
    shopping_habits: 'text-green-400 bg-green-500/10 border-green-500/20',
    entertainment: 'text-purple-400 bg-purple-500/10 border-purple-500/20',
    personality: 'text-cyan-400 bg-cyan-500/10 border-cyan-500/20',
    career_goals: 'text-orange-400 bg-orange-500/10 border-orange-500/20',
    decision_patterns: 'text-pink-400 bg-pink-500/10 border-pink-500/20'
  };

  const categoryLabels = {
    daily_routines: 'Daily Routines',
    shopping_habits: 'Shopping Habits',
    entertainment: 'Entertainment',
    personality: 'Personality',
    career_goals: 'Career Goals',
    decision_patterns: 'Decision Patterns'
  };

  return (
    <Card className="bg-gray-900/50 border-gray-800 hover:border-gray-700 transition-all duration-200">
      <CardHeader>
        <div className="flex items-center justify-between">
          <CardTitle className="text-base text-white">{question}</CardTitle>
          <span className={`text-xs px-2 py-1 rounded-lg border ${categoryColors[category] || 'text-gray-400 bg-gray-500/10 border-gray-500/20'}`}>
            {categoryLabels[category] || category}
          </span>
        </div>
      </CardHeader>
      <CardContent>
        <p className="text-gray-300 text-sm leading-relaxed mb-2">{answer}</p>
        {timestamp && (
          <p className="text-xs text-gray-500">
            {format(new Date(timestamp), 'MMM d, yyyy')}
          </p>
        )}
      </CardContent>
    </Card>
  );
};

export default BehaviorCard;