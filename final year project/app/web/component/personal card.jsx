import React from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';

const PersonalityCard = ({ title, traits, icon: Icon }) => {
  return (
    <Card className="bg-gray-900/50 border-gray-800 hover:border-cyan-500/50 transition-all duration-200">
      <CardHeader>
        <CardTitle className="flex items-center gap-2 text-white">
          {Icon && <Icon className="w-5 h-5 text-cyan-400" />}
          {title}
        </CardTitle>
      </CardHeader>
      <CardContent>
        <div className="flex flex-wrap gap-2">
          {traits && traits.length > 0 ? (
            traits.map((trait, index) => (
              <Badge
                key={index}
                variant="secondary"
                className="bg-cyan-500/10 text-cyan-400 border-cyan-500/20 hover:bg-cyan-500/20 transition-colors duration-200"
              >
                {trait}
              </Badge>
            ))
          ) : (
            <p className="text-gray-500 text-sm">No data available</p>
          )}
        </div>
      </CardContent>
    </Card>
  );
};

export default PersonalityCard;