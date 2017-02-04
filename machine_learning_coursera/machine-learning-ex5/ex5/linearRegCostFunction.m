function [J, grad] = linearRegCostFunction(X, y, theta, lambda)
%LINEARREGCOSTFUNCTION Compute cost and gradient for regularized linear 
%regression with multiple variables
%   [J, grad] = LINEARREGCOSTFUNCTION(X, y, theta, lambda) computes the 
%   cost of using theta as the parameter for linear regression to fit the 
%   data points in X and y. Returns the cost in J and the gradient in grad

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost and gradient of regularized linear 
%               regression for a particular choice of theta.
%
%               You should set J to the cost and grad to the gradient.
%


% Cost function
m = size(X, 1);	   		    % nb of training examples
predictions = X * theta;	% predictions of hypothesis on all m examples

sqrErrors = (predictions-y) .^2;	% squared errors


J = 1/(2*m) * sum(sqrErrors);

theta_0 = theta;
theta_0(1,:) = 0;
regularise = lambda/(2*m) * sum(theta_0 .^ 2); % the regularisation term
J = J + regularise;


% Gradient
grad = (1/m) .* (X' * (predictions - y));

regularise_grad = (lambda/m) * theta_0;
grad = grad + regularise_grad;

% =========================================================================

grad = grad(:);

end
