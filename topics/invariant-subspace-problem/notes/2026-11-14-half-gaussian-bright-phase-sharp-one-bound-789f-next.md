# 半高斯过渡层的 bright 相位：严格常数一与完整矩证书

日期：2026-11-14；工作标识：789f。

## 0. 结论和实际应用范围

令 \(U\) 在 \((0,\infty)\) 上具有密度
\[
 d\nu(u)=Z^{-1}\exp\left(-\lambda u-\frac\chi2u^2\right)du,
 \qquad \lambda\in\mathbb R,\quad \chi>0.
\]
记
\[
 \mu=\mathbb EU,\qquad
 q=\frac{\operatorname{Var}(U)}{\mu^2},\qquad
 \Delta=\frac{\mathbb EU^3}{\mu^3}
          -\left(\frac{\mathbb EU^2}{\mu^2}\right)^2.
\]
在真实平衡 star 端峰过渡层的完整源推导中，bright 与 dark 极限特征值分别为
\[
 \Lambda_{\rm b}
  =(1-q)^2+
       \frac{\big[\Delta/q-(1+q^2)\big]^2}{\Delta},
 \qquad
 \Lambda_{\rm d}=\frac{(1-q)^2}{1+q}.                     \tag{0.1}
\]
本稿证明一个独立的标量定理：
\[
 \boxed{0\leq\Lambda_{\rm b}<1,\qquad
                    0<\Lambda_{\rm d}<1.}               \tag{0.2}
\]
并且当 \(\lambda/\sqrt\chi\to-\infty\) 时，
\[
                \Lambda_{\rm b}\longrightarrow1,
                \qquad\Lambda_{\rm d}\longrightarrow1.   \tag{0.3}
\]
故统一常数 \(1\) 最优，但任意有限参数处都有严格余量。

证明只使用真实半高斯的积分分部、最高到七阶的矩，以及两条列出全部系数的有理多项式恒等式。没有将任意满足若干低阶矩约束的形式变量冒称为该分布，也没有用数值抽样判号。

本稿将已经保留完整物理源的过渡极限中的 \(4/3\) 上界收紧到 \(1\)。有限 \(Q\) 的结论仍须使用原完整运输的余项：若该余项在所述参数紧集上一致，则本稿的严格余量允许在充分大 \(Q\) 上得到原相位 \(\Phi_Q\preceq I\)。这不声称所有有限 \(Q\)、任意外场或退化 profile 的完整相位已经解决。

## 1. 归一化和真实矩递推

用 \(\sqrt\chi U\) 代替 \(U\) 不改变 \(q,\Delta\)，故只需证明 \(\chi=1\)。以下令
\[
 r_j=\frac{\mathbb EU^j}{\mu^j},\qquad r_0=r_1=1.
\]
对 \(u^j e^{-\lambda u-u^2/2}\) 积分分部，\(j\geq1\)，得到
\[
 \mathbb EU^{j+1}=j\mathbb EU^{j-1}-\lambda\mathbb EU^j.
                                                                  \tag{1.1}
\]
特别
\[
 \mathbb EU^2=1-\lambda\mu,
 \qquad
 \mathbb EU^3=2\mu-\lambda\mathbb EU^2.
\]
直接代入定义给
\[
                \boxed{\Delta=\frac{1-q}{\mu^2}.}         \tag{1.2}
\]
因为 \(U\) 的密度在整个正半轴严格为正，所有有限阶 Gram 矩阵
\([r_{i+j}]\) 以及 \([r_{i+j+1}]\) 都严格正定。这只是非零多项式不可能在正半轴上几乎处处为零。特别，\(\Delta>0\)，由 (1.2) 得 \(q<1\)；方差严格正给 \(q>0\)。

对密度本身的导数积分还给
\[
                     \lambda+\mu=Z^{-1}>0.
\]
于是
\[
 \operatorname{Var}(U)=1-\mu(\lambda+\mu)<1,
 \qquad
                         \Delta>q(1-q).                  \tag{1.3}
\]

令 \(d=1-q\)。递推 (1.1) 可完全写成 \(q,\Delta\) 的有理递推：
\[
 \boxed{
 r_{j+1}=\frac{j\Delta}{d}r_{j-1}
       -\left(\frac\Delta d-1-q\right)r_j,
       \qquad r_0=r_1=1.}                                \tag{1.4}
\]
因而下文每一个行列式都可由这个两项递推准确重建。

## 2. 保留到七阶的共同 Hankel 矩约束

由 (1.4) 逐项展开，得到以下三个恒等式：
\[
 \det[r_{i+j}]_{i,j=0}^{2}
       =\frac{\Delta\,[q(1+q)-\Delta]}{1-q},              \tag{2.1}
\]
\[
 \det[r_{i+j+1}]_{i,j=0}^{2}
       =\frac{\Delta^2\,[(3-q)\Delta-q(1+q)^2]}
                    {(1-q)^2},                          \tag{2.2}
\]
\[
 \det[r_{i+j+1}]_{i,j=0}^{3}
       =\frac{2\Delta^4}{(1-q)^5}\,\mathcal P(q,\Delta),  \tag{2.3}
\]
其中完整三次多项式为
\[
 \begin{split}
 \mathcal P(q,x)={}&x^3+(3q^2-18q+11)x^2\\
 &+(3q^4+3q^3-2q^2-q+1)x
        +q(q-1)(q+1)^4.                                 \tag{2.4}
 \end{split}
\]
严格正定性因此给
\[
 \frac{q(1+q)^2}{3-q}<\Delta<q(1+q),
 \qquad \mathcal P(q,\Delta)>0.                           \tag{2.5}
\]
单用 (1.3) 及 (2.5) 中的两个二次矩界会留下一个允许 \(\Lambda_{\rm b}>1\) 的形式区域。式 (2.3) 保留的真实较高矩正是以下中间区间所需的额外约束。

## 3. 将目标化成一个凹二次式

定义
\[
 \mathcal F(q,x)
        =xq^3(2-q)-(x-q-q^3)^2.                          \tag{3.1}
\]
由 (0.1) 准确得
\[
             1-\Lambda_{\rm b}
                    =\frac{\mathcal F(q,\Delta)}{q^2\Delta}.
                                                                  \tag{3.2}
\]
对每个固定 \(0<q<1\)，\(\mathcal F(q,x)\) 关于 \(x\) 严格凹。因此，只需给出包含真实 \(\Delta\) 的一个区间，并核两个端点的 \(\mathcal F\) 非负。

所有区间使用同一个严格上端 \(U(q)=q(1+q)\)。其值为
\[
 \mathcal F(q,U(q))=q^4(1+3q-2q^2)>0,
                         \qquad 0<q<1.                  \tag{3.3}
\]

### 3.1 小 \(q\)：\(0<q\leq1/5\)

取下端 \(L_0(q)=q(1-q)\)，由 (1.3) 有 \(\Delta>L_0(q)\)。而
\[
        \mathcal F(q,L_0(q))=q^4(1-5q)\geq0.              \tag{3.4}
\]
结合 (3.3)、严格凹性以及真实 \(\Delta\) 严格处于两个端点之间，得 \(\mathcal F(q,\Delta)>0\)。

### 3.2 中间 \(q\)：\(1/5\leq q\leq2/5\)

这时取
\[
                  L_1(q)=q-\frac75q^2+2q^3>0.             \tag{3.5}
\]
先证明真实 \(\Delta>L_1(q)\)。在本区间，\(\mathcal P(q,x)\) 的 \(x^2\) 和 \(x\) 系数都严格正；例如
\[
 3q^2-18q+11\geq107/25>0,
\]
\[
 3q^4+3q^3-2q^2-q+1\geq1-2q^2-q\geq7/25>0.
\]
所以 \(\mathcal P(q,x)\) 在 \(x\geq0\) 严格递增。直接代入 (3.5) 得
\[
 \mathcal P(q,L_1(q))=\frac{2q^2}{125}\,P_7(q),            \tag{3.6}
\]
\[
 P_7(q)=500q^7-300q^6-3690q^5+9121q^4
            -10475q^3+7535q^2-3025q+350.
\]
以下列出其在整个闭区间上的准确正系数证书。置
\(q=(1+2u)/(5(1+u))\)，\(u\geq0\)，则
\[
 \begin{split}
 -625(1+u)^7P_7\!\left(\frac{1+2u}{5(1+u)}\right)
 ={}&15000+230750u+991000u^2+2042121u^3\\
 &+2343093u^4+1541029u^5+545747u^6+80936u^7.
                                                               \tag{3.7}
 \end{split}
\]
所有系数严格正，右端点 \(q=2/5\) 用最高次系数或直接连续取极限。因此 \(P_7(q)<0\)，进而 \(\mathcal P(q,L_1(q))<0\)。与 \(\mathcal P(q,\Delta)>0\) 及严格单调性合用，得
\[
                              \Delta>L_1(q).              \tag{3.8}
\]
目标在此下端恰有因式分解
\[
 \mathcal F(q,L_1(q))
   =-\frac{q^4}{25}(5q-1)(10q^2-20q+1)\geq0,             \tag{3.9}
\]
因为本区间上第一因子非负、最后一因子严格负。又
\(L_1(q)<U(q)\)，差为 \(U-L_1=\frac{12}{5}q^2-2q^3>0\)。由 (3.3)、(3.8) 以及严格凹性，仍得 \(\mathcal F(q,\Delta)>0\)。

### 3.3 大 \(q\)：\(2/5\leq q<1\)

取 (2.5) 的下端
\[
                     L_2(q)=\frac{q(1+q)^2}{3-q}.
\]
准确代入为
\[
 \mathcal F(q,L_2(q))=\frac{q^2}{(3-q)^2}\,T_5(q),        \tag{3.10}
\]
\[
                 T_5(q)=q^5-13q^4+23q^3-11q^2+12q-4.
\]
置 \(q=(2+5u)/(5(1+u))\)、\(u\geq0\)，完整正系数身份为
\[
 \begin{split}
 3125(1+u)^5T_5\!\left(\frac{2+5u}{5(1+u)}\right)
 ={}&592+23660u+94075u^2\\
    &+148750u^3+102500u^4+25000u^5>0.                    \tag{3.11}
 \end{split}
\]
因此 (3.10) 严格为正。由 \(L_2(q)<\Delta<U(q)\) 和 (3.3)，再次得到 \(\mathcal F(q,\Delta)>0\)。

三个区间覆盖 \(0<q<1\)。结合 (3.2)，证明 \(\Lambda_{\rm b}<1\)。\(\Lambda_{\rm b}\geq0\) 直接来自 (0.1)，而 \(0<\Lambda_{\rm d}<1\) 来自 \(0<q<1\)。

## 4. 最优性、紧参数集与有限行余量

仍在 \(\chi=1\) 的归一化下，若 \(\lambda\to-\infty\)，则
\(\mu> -\lambda\)，而 \(\operatorname{Var}(U)<1\)，故
\[
                          0<q<\lambda^{-2}\longrightarrow0.
\]
由 \((1-q)^2\leq\Lambda_{\rm b}<1\) 即得 \(\Lambda_{\rm b}\to1\)，并且 \(\Lambda_{\rm d}\to1\)。恢复尺度就是 (0.3)。

所有矩随有限参数 \(\lambda/\sqrt\chi\) 连续。因此对任意紧参数集 \(K\subset\mathbb R\)，存在 \(\varepsilon_K>0\)，使
\[
 \max\{\Lambda_{\rm b},\Lambda_{\rm d}\}
             \leq1-\varepsilon_K,
             \qquad \lambda/\sqrt\chi\in K.              \tag{4.1}
\]
这不是全参数的严格余量；(0.3) 说明全参数不存在这样的正 \(\varepsilon\)。

若真实过渡运输已经在一个 profile 类中给出完整算子范数的一致余项 \(o(1)\)，且该类的 \(\lambda/\sqrt\chi\) 保持在固定紧集，那么 (4.1) 直接付掉该余项：充分大 \(Q\) 的原完整相位满足 \(\Phi_Q\preceq I\)。必须同时保留此前运输中的全部源、两个真实度量以及余项的一致性；不能只凭标量极限换成任意有限 \(Q\) 的断言。
