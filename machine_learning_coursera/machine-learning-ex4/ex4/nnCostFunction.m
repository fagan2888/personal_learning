function [J grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, ...
                                   X, y, lambda)
%NNCOSTFUNCTION Implements the neural network cost function for a two layer
%neural network which performs classification
%   [J grad] = NNCOSTFUNCTON(nn_params, hidden_layer_size, num_labels, ...
%   X, y, lambda) computes the cost and gradient of the neural network. The
%   parameters for the neural network are "unrolled" into the vector
%   nn_params and need to be converted back into the weight matrices. 
% 
%   The returned parameter grad should be a "unrolled" vector of the
%   partial derivatives of the neural network.
%

% Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
% for our 2 layer neural network
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));

% Setup some useful variables
m = size(X, 1);
         
% You need to return the following variables correctly 
J = 0;
Theta1_grad = zeros(size(Theta1));
Theta2_grad = zeros(size(Theta2));


% ====================== YOUR CODE HERE ======================
% Instructions: You should complete the code by working through the
%               following parts.
%
% Part 1: Feedforward the neural network and return the cost in the
%         variable J. After implementing Part 1, you can verify that your
%         cost function computation is correct by verifying the cost
%         computed in ex4.m
%

%%% 1. Randomly initialize the weights
% X dim 5000 x 400
% Theta1 dim 25 x 401
% Theta2 dim 10 x 26

%%% 2. Implement forward propagation to get hθ(x(i))
% First layer
a1 = [[ones(size(X,1), 1)], X]; % Add col of ones to X, a1 dim 5000 x 401
z2 = a1 * Theta1';  % z2 dim 5000 x 25

% Second layer
a2 = [[ones(size(z2,1), 1)], sigmoid(z2)]; % Add col of ones to a1, dim 26 x 5000
z3 = a2 * Theta2'; % a2 dim 10 x 5000
a3 = sigmoid(z3);

% neural networks predictions of hypothesis
[r_max, c_max] = max(a3, [], 2);  % row, column indices for max prob
p = c_max;                        % col index max == k == predicted class


%%% 3. Implement the cost function
% Project y to binary vector
k_class = max(y);
k_id = eye(k_class);
Y = k_id(y, :);		         % extract the column matching k

% J helper code
Theta1(:,1) = 0;             % excl the bias terms
thetas1 = sum(sum(Theta1 .^ 2));

Theta2(:,1) = 0;
thetas2 = sum(sum(Theta2 .^ 2));

regularise = lambda/(2*m) * (thetas1 + thetas2); % the regularisation term


J = J + (-1/m) * sum(sum(Y .* log(a3) + (1-Y) .* log(1 - a3)));
J = J + regularise;



% Part 2: Implement the backpropagation algorithm to compute the gradients
%         Theta1_grad and Theta2_grad. You should return the partial derivatives of
%         the cost function with respect to Theta1 and Theta2 in Theta1_grad and
%         Theta2_grad, respectively. After implementing Part 2, you can check
%         that your implementation is correct by running checkNNGradients
%
%         Note: The vector y passed into the function is a vector of labels
%               containing values from 1..K. You need to map this vector into a 
%               binary vector of 1's and 0's to be used with the neural network
%               cost function.
%
%         Hint: We recommend implementing backpropagation using a for-loop
%               over the training examples if you are implementing it for the 
%               first time.
%

%%% 4. Implement backpropagation to compute partial derivatives
% grad = (1/m) .* (X' * (p - y));
% grad = grad + (lambda/m .* theta_0);

% X dim 5000 x 400
% X(t,:) dim 1 x 400
% Theta1 dim 25 x 401
% Theta2 dim 10 x 26

% deltas_1 = zeros(size(X));
% deltas_2 = zeros(size(Theta1));
% deltas_3 = zeros(size(Theta2));

% % Project y to binary vector
% k_class = max(y);
% k_id = eye(k_class);
% Y = k_id(y, :);		         % extract the column matching k

% acc_a_1 = zeros(size());

% for t = 1:m,
% 	% Forward propagation first layer
% 	a_1 = X(t,:);		  % a_1 dim 1 x 400
% 	a_1 = [1 a_1];		  % a_1 dim 1 x 401 w/bias
% 	z_2 = a_1 * Theta1';  % z_2 dim 1 x 25
% 	% Forward propagation second layer
% 	a_2 = [[ones(size(z_2,1), 1)], sigmoid(z_2)]; % a_2 dim 1 x 26 w/bias
% 	z_3 = a_2 * Theta2';	  % z_3 dim 5000 x 10
% 	a_3 = sigmoid(z3);

% 	% Error term for first layer
% 	for k = 1:num_labels,
% 		delta_3 = a_3 - Y(t,:);      % dim 5000 x 10
% 		delta_2 = (delta_3 * Theta2) .* sigmoidGradient([ones(size(z_2, 1)) z_2]); % dim 5000 x 26
% 									 % dim 5000 x 26	
% 		delta_2 = delta_2(:, 2:end); % dim 5000 x 25 -> removing bias

% 	end

% 	acc_a_1 = 
% 	% accumulate the  deltas together
% 	deltas1 = (delta_2' * a_1);
% 	deltas2 = (delta_3' * a_2);

% end

% Error term for first layer
for k = 1:num_labels,
	delta_3 = a3 .- Y;      % dim 5000 x 10
	delta_2 = (delta_3 * Theta2) .* sigmoidGradient([ones(size(z2, 1), 1) z2]); % dim 5000 x 26
									 % dim 5000 x 26	
	delta_2 = delta_2(:, 2:end); % dim 5000 x 25 -> removing bias
end

deltas1 = (delta_2' * a1);
deltas2 = (delta_3' * a2);


% Part 3: Implement regularization with the cost function and gradients.
%
%         Hint: You can implement this around the code for
%               backpropagation. That is, you can compute the gradients for
%               the regularization separately and then add them to Theta1_grad
%               and Theta2_grad from Part 2.
%

regularise1 = (lambda / m) * [zeros(size(Theta1, 1), 1) Theta1(:, 2:end)];
regularise2 = (lambda / m) * [zeros(size(Theta2, 1), 1) Theta2(:, 2:end)];
Theta1_grad = deltas1 ./ m + regularise1;
Theta2_grad = deltas2 ./ m + regularise2;


%%% 5. Use gradient checking to confirm that your backpropagation works. 
%%%    Then disable gradient checking.



% -------------------------------------------------------------

% =========================================================================

% Unroll gradients
grad = [Theta1_grad(:) ; Theta2_grad(:)];


end
