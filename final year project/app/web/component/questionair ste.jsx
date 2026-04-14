import React from 'react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Textarea } from '@/components/ui/textarea';
import { Label } from '@/components/ui/label';
import { Progress } from '@/components/ui/progress';
import { ChevronLeft, ChevronRight } from 'lucide-react';

const QuestionnaireStep = ({
  step,
  totalSteps,
  title,
  questions,
  answers,
  onAnswerChange,
  onNext,
  onPrevious,
  isLastStep
}) => {
  const progress = ((step + 1) / totalSteps) * 100;

  const handleSubmit = (e) => {
    e.preventDefault();
    onNext();
  };

  return (
    <div className="w-full max-w-2xl mx-auto">
      <div className="mb-8">
        <div className="flex items-center justify-between mb-2">
          <span className="text-sm text-gray-400">
            Step {step + 1} of {totalSteps}
          </span>
          <span className="text-sm text-cyan-400 font-medium">
            {Math.round(progress)}% Complete
          </span>
        </div>
        <Progress value={progress} className="h-2" />
      </div>

      <div className="bg-gray-900/50 rounded-2xl p-8 border border-gray-800">
        <h2 className="text-2xl font-bold text-white mb-6" style={{ letterSpacing: '-0.02em' }}>
          {title}
        </h2>

        <form onSubmit={handleSubmit} className="space-y-6">
          {questions.map((question, index) => (
            <div key={index} className="space-y-2">
              <Label htmlFor={`question-${index}`} className="text-gray-200 font-medium">
                {question.text}
              </Label>
              {question.type === 'textarea' ? (
                <Textarea
                  id={`question-${index}`}
                  value={answers[question.id] || ''}
                  onChange={(e) => onAnswerChange(question.id, e.target.value)}
                  placeholder={question.placeholder}
                  className="bg-gray-800 border-gray-700 text-white placeholder:text-gray-500 min-h-[100px]"
                  required
                />
              ) : (
                <Input
                  id={`question-${index}`}
                  type={question.type || 'text'}
                  value={answers[question.id] || ''}
                  onChange={(e) => onAnswerChange(question.id, e.target.value)}
                  placeholder={question.placeholder}
                  className="bg-gray-800 border-gray-700 text-white placeholder:text-gray-500"
                  required
                />
              )}
            </div>
          ))}

          <div className="flex items-center justify-between pt-4">
            <Button
              type="button"
              onClick={onPrevious}
              disabled={step === 0}
              variant="ghost"
              className="text-gray-400 hover:text-white disabled:opacity-50 disabled:cursor-not-allowed"
            >
              <ChevronLeft className="w-4 h-4 mr-2" />
              Previous
            </Button>

            <Button
              type="submit"
              className="bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-600 hover:to-blue-700 text-white"
            >
              {isLastStep ? 'Complete' : 'Next'}
              {!isLastStep && <ChevronRight className="w-4 h-4 ml-2" />}
            </Button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default QuestionnaireStep;