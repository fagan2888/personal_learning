
% % Test for linearRegCostFunction()
% X = [[1 1 1]' magic(3)];
% y = [7 6 5]';
% theta = [0.1 0.2 0.3 0.4]';
% [J g] = linearRegCostFunction(X, y, theta, 7)


% % Test for learningCurve()
% X = [ones(5,1) reshape(-5:4,5,2)];
% y = [-2:2]';
% Xval=[X;X]/10;
% yval=[y;y]/10;
% [et ev] = learningCurve(X,y,Xval,yval,1)


% % Test for polyFeatures()
% polyFeatures([1:3]',4)


% Test for validationCurve()
X = [1 2 ; 1 3 ; 1 4 ; 1 5]
y = [7 6 5 4]'
Xval = [1 7 ; 1 -2]
yval = [2 12]'
[lambda_vec, error_train, error_val] = validationCurve(X,y,Xval,yval )
