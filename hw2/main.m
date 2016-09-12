
function main()
    function y = ibin(n,m)
        y = factorial(n)/(factorial(m)*factorial(n-m));
    end

    function y = jbin(n,m)
        y =   prod((n-m+1:n)./(1:m));
    end    

    function y = kbin(n,m)
        T = pascal(max(n-m,m)+1);
        y = T(n-m+1,m+1);
    end
    format compact
    s0 = sprintf('i j answer 1, answer 2, answer 3');
    s1 = sprintf('%d %d      %d       %d         %d',2 ,1, ibin(2,1),jbin(2,1),kbin(2,1));
    s2 = sprintf('%d %d      %d      %d        %d',5 ,2, ibin(5,2),jbin(5,2),kbin(5,2));
    disp(s0);
    disp(s1);
    disp(s2);

end