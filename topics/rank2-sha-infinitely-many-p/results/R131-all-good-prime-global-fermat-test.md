# R131. 不要求普通性的两个全局 Fermat 商证书

日期：2026-11-12。**状态：已证明，已独立复核；实际测试的无穷非零性仍开。**

对 R119/R126 的固定 \(E:y^2=x^3-17x\)、\(F=\mathbb Q(\sqrt{-15})\) 和实际
\(L/F\)、\(Q\)，删去固定有限例外素数后，以下充分证书适用于所有好素数 \(p\)，
包括超奇异和 \(F\)-惰性情形。

取 \(\tau\) 生成 \(\operatorname{Gal}(L/F)\)。若 \(p\) 在 \(F\) 分裂，令 \(s\) 是
一个 \(p\) 上素位的 Artin 元，取
\[
 D_p=(s^2-a_ps+p)(s^{-2}-a_ps^{-1}+p).
\]
若 \(p\) 在 \(F\) 惰性，取 \(D_p=(p+1)^2-a_p^2\)。
两者都为实际整群环算子和 \(\mathbb Z_p[\zeta_p]\) 单位。
\(R=12D_pQ\) 在全部 \(p\) 处形式群及坏位恒等组件中，保留原 \(\delta\) 指数 \(a\)。

对这样的实际点定义非零有理 \(p\) 单位
\[
 \nu(P)=\frac{N_{L/\mathbb Q}(-x(P)/y(P))}
                    {N_{L/\mathbb Q}\mathfrak d(P)},\qquad
 z_j=\frac{\nu(R+\tau^jR)}{\nu(R)^2},\qquad
 q_p(z)=\frac{z^{p-1}-1}{p}\pmod p,
\]
其中 \(\mathfrak d(P)\) 是横坐标分母理想的平方根。
则
\[
 \boxed{\left(\sum_{j=1}^{(p-1)/2}j^2q_p(z_j),\
              \sum_{j=1}^{(p-1)/2}j^4q_p(z_j)\right)\ne(0,0)
        \quad\Longrightarrow\quad \Sha(E/\mathbb Q)[p^\infty]=0.}
\]

证明以固定有理 Bernardi sigma 替代普通 sigma：
\(D^2\log\sigma_0=-x\)，两次形式积分直接给
\(\sigma_0(t)/t\in1+p^4\mathcal O\) 于本题的不分歧 \(p\) 盘。
形式加法、乘法恒等式与全部地方的 norm/分母项给真正的整双线性全局高度。
其整角色 \(\mathcal R_R\) 满足 \(v_\delta\mathcal R_R\ge2a\)，而上述两矩非零
给 \(v_\delta\mathcal R_R<4\)，所以 \(a\le1\)。R122/R125 的准确维数与长度比较
随后给原曲线初级 Sha 为零。

论证无需这个高度非退化，也无需先付 \(a\) 偶或两个局部符号。
它使 R126 的无穷输入全部进入测试范围；测试的无穷非零性仍待证明。

完整解析估计、全局二次性及原始来源：
[Bernardi 高度与全好素数测试](../notes/2026-11-12-bernardi-height-and-all-good-prime-fermat-test.md)。
