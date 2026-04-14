import React from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Progress } from '@/components/ui/progress';
import { Lightbulb, TrendingUp } from 'lucide-react';

const SimulationResult = ({ scenario, prediction, reasoning, confidence, timestamp }) => {
  const getConfidenceColor = (conf) => {
    if (conf >= 80) return 'text-green-400 bg-green-500/10 border-green-500/20';
    if (conf >= 60) return 'text-yellow-400 bg-yellow-500/10 border-yellow-500/20';
    return 'text-orange-400 bg-orange-500/10 border-orange-500/20';
  };

  return (
    <Card className="bg-gray-900/50 border-gray-800 hover:border-cyan-500/50 transition-all duration-200">
      <CardHeader>
        <div className="flex items-start justify-between gap-4">
          <CardTitle className="text-white text-lg leading-snug">
            {scenario}
          </CardTitle>
          <Badge className={`${getConfidenceColor(confidence)} border`}>
            {confidence}% confident
          </Badge>
        </div>
      </CardHeader>
      <CardContent className="space-y-4">
        <div>
          <div className="flex items-center gap-2 mb-2">
            <TrendingUp className="w-4 h-4 text-cyan-400" />
            <span className="text-sm font-medium text-gray-400">Prediction</span>
          </div>
          <p className="text-gray-200 leading-relaxed">{prediction}</p>
        </div>

        {reasoning && (
          <div>
            <div className="flex items-center gap-2 mb-2">
              <Lightbulb className="w-4 h-4 text-cyan-400" />
              <span className="text-sm font-medium text-gray-400">Reasoning</span>
            </div>
            <p className="text-gray-300 text-sm leading-relaxed">{reasoning}</p>
          </div>
        )}

        <div>
          <div className="flex items-center justify-between mb-2">
            <span className="text-xs text-gray-500">Confidence Level</span>
            <span className="text-xs text-gray-400">{confidence}%</span>
          </div>
          <Progress value={confidence} className="h-2" />
        </div>
      </CardContent>
    </Card>
  );
};

export default SimulationResult;