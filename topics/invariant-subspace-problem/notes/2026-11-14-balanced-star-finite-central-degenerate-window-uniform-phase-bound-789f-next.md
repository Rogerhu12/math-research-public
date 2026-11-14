# 平衡 star 中央退化窗口：全部有限行、完整源的显式统一相位界

日期：2026-11-14；工作标识：789f。

## 0. 已完成的范围与常数

先将全部小组展开为 \(Q\) 个真实二值坐标。给定正权平方
\(z_1,\ldots,z_Q\)，假设固定常数满足
\[
 0<a\leq z_i\leq b<\infty,\qquad
 \left|\sum_{i=1}^Q(z_i-1)\right|\leq D,\qquad
 \sum_{i=1}^Q(z_i-1)^2\leq S_0.                            \tag{0.1}
\]
这里 \(D,S_0\geq0\) 固定，\(Q\) 任意。允许少数权始终离开 \(1\)；不要求每个 \(z_i\to1\)，也不要求各个组的长度占固定正比例。

沿原平衡 star 的真实概率模型，令
\[
 F(t)=\prod_{i=1}^Q(1-t+z_it),\qquad
 \rho(t)=\frac{F(t)}{\int_0^1F(u)\,du},\qquad 0<t<1.
\]
给定 \(T=t\)，令各 \(X_i\) 独立，且
\[
 \Pr(X_i=1\mid T=t)=p_i(t)=\frac{z_it}{1-t+z_it}.
\]
定义全部真实二值源上的形式
\[
 m=\mathbb EX,\qquad y=2m-\mathbf1,\qquad
 G=\operatorname{Cov}(X),
\]
\[
 H=\mathbb E\frac{1-T}{T}XX^*,\qquad
 L=\mathbb E\frac{T}{1-T}(\mathbf1-X)(\mathbf1-X)^*,
\]
\[
                    J=HG^{-1}L-2G-yy^*.                  \tag{0.2}
\]
这些是原相位的同一源概率形式；与物理形式之间的同一个正标量不影响目标。端点乘积按实际 Bernoulli 源计算，以下给出的条件形式会显式消去可能误读的分母。

置
\[
 \ell=\min\{1,a\},\qquad u=\max\{1,b\},\qquad
 K^2=\frac{S_0}{\ell^2},\qquad
 r=\exp\left(-2D-\frac{S_0}{2\ell^2}\right),              \tag{0.3}
\]
\[
 c_* =\frac{a r^2}{24u^2(1+K^2)},\qquad
 C_* =1+\frac b{\ell^2}+K^2,
 \qquad \Theta=\frac{C_*}{c_*}.                           \tag{0.4}
\]
则对全部满足 (0.1) 的有限 \(Q\)，有
\[
 \boxed{J^*L^{-1}J\preceq
       \kappa(a,b,D,S_0)H,
       \qquad \kappa=(\Theta^2+3\Theta)^2.}               \tag{0.5}
\]
常数完全明确，不依赖 \(Q\)、组数或组大小。它是保守常数，本文没有声称最优值 \(1\)。

## 1. 真正密度及统一矩下界

写 \(c_i=z_i-1\)、\(A=\sum_i c_i\)、\(S=\sum_i c_i^2\)，并令
\(L_i(t)=1+t c_i\)。始终有 \(\ell\leq L_i(t)\leq u\)。由 \(\log\) 的二阶余项及 \(\log(1+x)\leq x\)，
\[
 tA-\frac{t^2S}{2\ell^2}
            \leq\log F(t)\leq tA.
\]
因此
\[
 -D-\frac{S_0}{2\ell^2}\leq\log F(t)\leq D,
                 \qquad \rho(t)\geq r.                   \tag{1.1}
\]
这里只用了真实乘积密度；没有改为任意集中的外加混合分布。

令 \(a_0(t)=t(1-t)\)。由 (1.1) 得
\[
 \mathbb Ea_0(T)\geq r/6,
 \qquad \mathbb ET^2,\ \mathbb E(1-T)^2\geq r/3.          \tag{1.2}
\]
而
\[
 \operatorname{Var}(T)
 =\min_{c\in\mathbb R}\mathbb E(T-c)^2
 \geq r\min_{c\in\mathbb R}\int_0^1(t-c)^2dt
 =r/12.                                                  \tag{1.3}
\]
不论 \(\rho\) 的均值位于何处，(1.3) 都成立。

## 2. 完整二值源的同一公共度量

使用
\[
                       \mathcal D=I+\mathbf1\mathbf1^*.
\]
我们将证明
\[
 \boxed{c_*\mathcal D\preceq H,G,L\preceq C_*\mathcal D,
                  \qquad yy^*\preceq C_*\mathcal D.}     \tag{2.1}
\]
各式都在完整 \(Q\) 维二值源上成立。后文只对这一个共同度量作合同；没有分别将三个非交换矩阵标量化。

固定任意 \(v\in\mathbb C^Q\)，记 \(\alpha=v^*\mathbf1\)。定义真实误差向量
\[
 r_i(t)=\frac{t(1-t)c_i}{L_i(t)},\qquad
 \delta_{H,i}(t)=\frac{(1-t)c_i}{L_i(t)},\qquad
 \delta_{L,i}(t)=-\frac{t c_i}{L_i(t)}.
\]
有
\[
 p(t)=t\mathbf1+r(t),\qquad
 p(t)=t(\mathbf1+\delta_H(t)),\qquad
 \mathbf1-p(t)=(1-t)(\mathbf1+\delta_L(t)),
\]
\[
 \|r(t)\|\leq K/4,
 \qquad \|\delta_H(t)\|,\|\delta_L(t)\|\leq K.             \tag{2.2}
\]

条件 Bernoulli 方差严格给出
\[
 \begin{split}
 v^*Hv={}&\mathbb E a_0(T)
             |\alpha+v^*\delta_H(T)|^2\\
   &+\sum_i|v_i|^2
           \mathbb E\frac{z_i(1-T)^2}{L_i(T)^2},           \tag{2.3}
 \end{split}
\]
\[
 \begin{split}
 v^*Lv={}&\mathbb E a_0(T)
             |\alpha+v^*\delta_L(T)|^2\\
   &+\sum_i|v_i|^2
           \mathbb E\frac{z_iT^2}{L_i(T)^2},               \tag{2.4}
 \end{split}
\]
\[
 \begin{split}
 v^*Gv={}&\operatorname{Var}
              \big(T\alpha+v^*r(T)\big)\\
   &+\sum_i|v_i|^2
           \mathbb E\frac{z_i a_0(T)}{L_i(T)^2}.           \tag{2.5}
 \end{split}
\]
所有交叉项都保存在这些完整平方或真实方差中。

### 2.1 \(H,L\) 的下界

先以 \(H\) 为例，记 (2.3) 首项为 \(B_H\)，并令
\(\beta=\mathbb Ea_0(T)\geq r/6\)。三角不等式与 (2.2) 给
\[
 \sqrt\beta\,|\alpha|
 \leq\sqrt{B_H}+\sqrt\beta\,K\|v\|,
\]
故
\[
 \|v\|^2+|\alpha|^2
 \leq(1+2K^2)\|v\|^2+\frac{12}{r}B_H.                   \tag{2.6}
\]
第二项的真实噪声至少为
\[
                   \eta_H\|v\|^2,
                   \qquad \eta_H=\frac{a r}{3u^2}.        \tag{2.7}
\]
于是
\[
 H\succeq
   \min\left\{\frac{a r}{3u^2(1+2K^2)},\frac r{12}\right\}
                      \mathcal D.                        \tag{2.8}
\]
\(L\) 的证明由 (2.4) 完全同样成立。

### 2.2 \(G\) 的下界；保留真实中心化

记 (2.5) 的方差项为 \(B_G\)。在中心化后的 \(L^2(\rho)\) 中，
\[
 |\alpha|\sqrt{\operatorname{Var}(T)}
       \leq\sqrt{B_G}+\sqrt{\operatorname{Var}(v^*r(T))}
       \leq\sqrt{B_G}+\frac K4\|v\|.
\]
使用 (1.3) 得
\[
 \|v\|^2+|\alpha|^2
 \leq\left(1+\frac{3K^2}{2r}\right)\|v\|^2
                       +\frac{24}{r}B_G.                \tag{2.9}
\]
真实条件噪声至少为 \(\eta_G\|v\|^2\)，其中
\(\eta_G=a r/(6u^2)\)。所以
\[
 G\succeq
 \min\left\{\frac{a r^2}{3u^2(2r+3K^2)},\frac r{24}\right\}
                         \mathcal D.                     \tag{2.10}
\]
这一步控制的是完整协方差，而非未中心化的第二矩。

由于 \(0<r\leq1\)、\(a\leq u^2\)，(0.4) 的 \(c_*\) 不超过 (2.8) 和 (2.10) 的每个候选常数。例如
\[
 \frac{c_*}{a r^2/[3u^2(2r+3K^2)]}
       =\frac{2r+3K^2}{8(1+K^2)}\leq\frac38,
 \qquad
 \frac{c_*}{r/24}
       =\frac{a r}{u^2(1+K^2)}\leq1.
\]
因此 (2.1) 的三个下界已经证明。

### 2.3 共同上界及硬源平方

由 \(a_0\leq1/4\)、(2.2) 和 (2.3)–(2.4)，
\[
 H,L\preceq
       \left(\frac b{\ell^2}+\frac{K^2}{2}\right)I
                         +\frac12\mathbf1\mathbf1^*.     \tag{2.11}
\]
由 \(\operatorname{Var}(T)\leq1/4\) 与 (2.5)，
\[
 G\preceq
       \left(\frac b{4\ell^2}+\frac{K^2}{8}\right)I
                         +\frac12\mathbf1\mathbf1^*.     \tag{2.12}
\]
又
\[
 y=(2\mathbb ET-1)\mathbf1+2\mathbb Er(T),
\]
所以
\[
                    yy^*\preceq\frac{K^2}{2}I
                                  +2\mathbf1\mathbf1^*.  \tag{2.13}
\]
总有 \(b/\ell^2\geq1\)：若 \(a\geq1\) 则 \(\ell=1,b\geq1\)；若 \(a<1\)，则 \(b/\ell^2\geq1/a>1\)。因此 (0.4) 的同一个 \(C_*\) 同时支付 (2.11)–(2.13)，完成 (2.1)。

## 3. 保持原乘法顺序的完整相位界

对所有形式只作同一个合同：
\[
 \widehat H=\mathcal D^{-1/2}H\mathcal D^{-1/2},\quad
 \widehat G=\mathcal D^{-1/2}G\mathcal D^{-1/2},\quad
 \widehat L=\mathcal D^{-1/2}L\mathcal D^{-1/2},\quad
 \widehat y=\mathcal D^{-1/2}y.
\]
由 (2.1)，
\[
 c_*I\preceq\widehat H,\widehat G,\widehat L\preceq C_*I,
                \qquad\widehat y\widehat y^*\preceq C_*I.
\]
特别，原有序乘积准确变为
\[
 \widehat J:=\mathcal D^{-1/2}J\mathcal D^{-1/2}
    =\widehat H\widehat G^{-1}\widehat L
                       -2\widehat G-\widehat y\widehat y^*.
                                                                  \tag{3.1}
\]
这里没有交换 \(H,G,L\) 的次序，也没有把三个独立谱界直接相乘后冒称 Loewner 序。是在同一个归一化源上使用实际算子范数，得到
\[
                  \|\widehat J\|\leq C_*^2/c_*+3C_*.
\]
于是
\[
 \widehat J^*\widehat L^{-1}\widehat J
 \preceq\frac{(C_*^2/c_*+3C_*)^2}{c_*}I
 \preceq\frac{(C_*^2/c_*+3C_*)^2}{c_*^2}\widehat H.
\]
恢复公共合同就是 (0.5)。

## 4. 任意分组与全部真实源度量

现在将相同权值的坐标分成任意多组，组长度 \(q_i\geq1\)，组权平方为 \(z_i\)，\(\sum_i q_i=Q\)。条件 (0.1) 就是
\[
 0<a\leq z_i\leq b,\qquad
 \left|\sum_iq_i(z_i-1)\right|\leq D,\qquad
 \sum_iq_i(z_i-1)^2\leq S_0.                              \tag{4.1}
\]
实际组源为 \(\overline X_i=K_i/q_i\)。记 \(S\) 为把一个组向量重复到全体位的映射，\(D_q=\operatorname{diag}(q_i)\)，则
\(E=S D_q^{-1/2}\) 是到完整二值源的等距嵌入。全部 \(H,G,L,yy^*\) 都在组内置换下不变，所以 \(\operatorname{Ran}E\) 是它们的共同 reducing 子空间；完整逆也保持这个子空间。

若组源形式记作 \(H_{\rm grp},G_{\rm grp},L_{\rm grp},y_{\rm grp}\)，则
\[
 E^*H E=D_q^{1/2}H_{\rm grp}D_q^{1/2},
\]
\(G,L\) 同样，且 \(E^*y=D_q^{1/2}y_{\rm grp}\)。因而完整相位 (0.5) 限制到该 reducing 子空间，再作真实源合同，恰给同一个 \(\kappa\) 的组源相位界。

公共度量在组源坐标中准确为
\[
                        \mathcal D_q=D_q^{-1}
                                        +\mathbf1\mathbf1^*,
\]
而不是把各组平均误当作等距源。所有常数仍与组数、各 \(q_i\) 和 \(Q\) 无关。

## 5. 与过渡、原问题接口的边界

本定理是全部有限 \(Q\) 的真实相位界，不仅是一个 \(Q\to\infty\) 极限。它覆盖总漂移及累计平方偏差同时有界的中央退化类，并允许固定数量的固定离群权。它与需曲率下界的内峰或半高斯过渡定理使用不同的参数区间。

本文不把 (0.1) 外推为任意正权的统一 \(\kappa\)，也不声称原连续尾 moving-birth 的所有源都满足 (0.1)。若要应用于另一权族，必须实际支付同一归一化下的 \(a,b,D,S_0\)，以及对应的完整源识别。原 graph 的跨出生与固定测试回归仍不能由此自动省略。
