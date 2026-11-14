# R239 附录：四异常权模型的整个高度二 primitive 严格比较

日期：2026-11-13  
作者：AI 协作研究，central_review  
状态：已证明；root 已独立全文核验短池维数、三参数完整 MP、全部正交块，并执行完整 BigInt 证书通过。

## 1. 两个准确结论

先取四个任意正头权 a_1,…,a_4 和两个单位权池位，
$$
D=\sum_{i=1}^4a_iE_i+D_{\mathrm w}.
$$
在弱池置换固定部分取相对出生 s=2。固定 primitive 块的维数为六；整个六位 K_2 的维数是九，二者不能混同。串长 h=6−2s=2，只有相邻阶 n=1。

按完整孔层先取
$$
F_n=\frac{D^n(D^*)^n}{(n!)^2}
$$
的逆，再压缩，得到真正的 Γ_n。

**定理 1（六维短块）。**
$$
\boxed{\Gamma_1\Gamma_2^{-1}\Gamma_1<\Gamma_0.}
\tag{1.1}
$$

再取四个任意正头权，加任意偶数 M≥0 个单位权池位，令
$$
N=M+4,\qquad s=(N-2)/2=(M+2)/2.
$$
这时整个 K_s 的串长为 h=2。

**定理 2（整个 h=2 primitive）。** 在整个 K_s 上严格有
$$
\boxed{\Gamma_1\Gamma_2^{-1}\Gamma_1<\Gamma_0.}
\tag{1.2}
$$
定理 2 在 §7 中逐块拼合。本文不声称 h≥3 的全部近端阶数，也不从这些有限正权模型推出一般无限尾结论。

## 2. L<q 时重做源空间、可行参数与端点

此处 q=4、L=2，不能直接援用要求 L≥q 的一般出生维数模板。以下单独支付。

令头缺失集合为 R，r=|R|。池向量为
$$
w_k=\sum_{|J|=k}e_J,\qquad \|w_k\|^2=\binom2k.
$$
源坐标是六个复数 x_ij，写齐次二次多重仿射式
$$
f(X)=\sum_{1\le i<j\le4}x_{ij}X_iX_j,\qquad
f(R)=\sum_{\{i,j\}\subseteq R}x_{ij}.
$$
准确 primitive 源为
$$
\boxed{
g(f)=\sum_{2\le r\le4}
(-1)^{r-2}\frac{a_R}{\binom2{r-2}} f(R)\,
e_{[4]\setminus R}w_{r-2}.
}
\tag{2.1}
$$
因为
$$
\sum_{i\in R}f(R\setminus\{i\})=(r-2)f(R),
$$
头删除与池删除逐项相消，Dg=0。r=2 的六个系数 a_Rx_R 独立任意。

源层固定空间维数为 6+4+1=11，下一低层固定空间维数为 4+1=5。固定删除满射，所以固定 primitive 维数为六，(2.1) 穷尽它。这里的满射可从完整无权 Boolean 层的 sl(2) 分解得到，再用正权对角相似及池置换平均；对相邻层 H_2→H_1，亦可直接在目标 H_1 上用无权关系 DD*−D*D=4I 验证。

对 n=0,1,2，输入合法状态为
$$
0\le n+r-2\le2.
$$
令 F=f+p，其中 p 次数至多一，并要求 F 在非法状态上为零。构造
$$
u_n(F)=\sum_{\substack{R\subseteq[4]\\0\le n+r-2\le2}}
(-1)^{r-2}\frac{a_R}{\binom2{n+r-2}}F(R)\,
e_{[4]\setminus R}w_{n+r-2}.
\tag{2.2}
$$
准确有 D^n u_n(F)/n!=g(f)。读目标集合 R，二项式相消后为
$$
\frac{a_R}{2^{\underline{r-2}}}
\sum_{T\subseteq R}(-1)^{|T|-2}
(n+|T|-2)^{\underline{r-2}}F(T).
\tag{2.3}
$$
非法 T 的 F(T)=0，故扩和合法。二次最高部分给
(-1)^(r−2)(r−2)! 的有限差分，低次 p 全部消去，正好恢复 (2.1)。

三个阶数的参数必须分别处理：

- n=0：非法 r=0,1 迫 p=0，只有源自身。
- n=1：非法状态同时是 ∅ 和 [4]。准确约束为
  $$
  p(0)=0,\qquad \sum_i b_i=-f([4]),
  \quad p(X)=\sum_i b_iX_i.
  \tag{2.4}
  $$
  因而只有三个自由参数。
- n=2：非法 r=3,4，唯一可行式为
  $$
  F(X)=f(1-X).
  \tag{2.5}
  $$
  它的最高齐次部分仍是 f。

n=1 的固定输入维数为 4+6+4=14，固定目标维数为 11；完整删除 H_3→H_2 满射，平均后固定部分仍满射。因此解空间维数为三。(2.4) 给出的三参数解映射单射：输入为零使 F 在全部合法状态为零，非法状态本已为零，多重仿射唯一性便迫 F=0。故已穷尽全部固定解。

n=2 的固定输入和目标均为十一维。完整 D²:H_4→H_2 为加权 Boolean Lefschetz 同构，固定部分亦为同构；(2.5) 是唯一固定解。该完整同构不依赖 L≥q：无权六位模型按出生 0,1,2 的标准正交字符串分解，每条 D² 的相应系数非零；正权对角相似保留可逆性。

最后，任意全空间可行解可先删去无用孔层，再作两位池的正交置换平均，源不变且范数不增。因此上述参数最小化确给全 Hilbert Moore–Penrose 范数，并非只在固定空间选择一个试探逆。

## 3. 三个 Gram 与三参数真实 Schur 补

置 z_i=a_i²>0，z_R=∏_(i∈R)z_i。按边序
$$
12,\ 13,\ 14,\ 23,\ 24,\ 34
$$
排列六维源坐标。令 v_R∈ℝ⁶ 的分量为
$$
(v_R)_{ij}=1_{\{i,j\}\subseteq R},\qquad
v_R^{\,c}=v_{R^c}.
$$
H_n 是 (2.2) 的完整 MP Gram。两端准确为
$$
H_0=\sum_{r=2}^4\frac{z_R}{\binom2{r-2}}\,v_Rv_R^T,
\qquad
H_2=\sum_{r=0}^2\frac{z_R}{\binom2r}\,v_R^{\,c}(v_R^{\,c})^T.
\tag{3.1}
$$

为参数化 (2.4)，写
$$
F(X)=f(X)-f([4])X_4+\sum_{i=1}^3\beta_i(X_i-X_4).
$$
在状态 R 上，令
$$
\widehat v_R=v_R-1_{\{4\in R\}}{\bf1}_6,\qquad
u_R=(1_{\{i\in R\}}-1_{\{4\in R\}})_{i=1}^3.
$$
于是 F(R)=v̂_R^T x+u_R^Tβ。对 1≤r≤3 定义整数权
$$
w_R=\frac{2z_R}{\binom2{r-1}}=
\begin{cases}2z_R,&r=1,3,\\ z_R,&r=2.\end{cases}
$$
置
$$
S=\sum_Rw_R\widehat v_R\widehat v_R^T,\quad
M=\sum_Rw_R\widehat v_Ru_R^T,\quad
C=\sum_Rw_Ru_Ru_R^T.
\tag{3.2}
$$
C>0，因为三个单点状态 {1},{2},{3} 给三个正坐标项。故完整最小化准确给
$$
\boxed{2H_1=S-MC^{-1}M^T.}
\tag{3.3}
$$

写
$$
A=2H_0,\quad B=2H_2,\quad \Delta=\det C,\quad
K=\Delta S-M\,\operatorname{adj}(C)\,M^T.
$$
A、B、C 都严格正定，Δ>0。六个 r=2 状态分别给 A、B 的六个正坐标项；这一点也支付 detB>0。于是
$$
H_1=\frac{K}{2\Delta}
$$
且
$$
\boxed{
H_0-H_1H_2^{-1}H_1
=\frac{\mathcal P(z)}{2\Delta^2\det B},
\quad
\mathcal P(z)=\Delta^2\det(B)A-K\,\operatorname{adj}(B)\,K.
}
\tag{3.4}
$$
所有矩阵乘法顺序保留，尤其没有将真实三个低次参数的 Schur 补换成逐系数最小化。

## 4. 完整可执行整数证书

代码见：

[四头两池六维 BigInt 证书](../notes/2026-11-13-four-exceptional-weights-two-pool-six-dimensional-certificate-central-review.mjs)

完整源 blob：
$$
\texttt{4c005194bb5d6cd79dca8c864bd560f0ec5521d3}.
$$

脚本从十六个子集直接构造 (3.1)—(3.4)。B 使用十一列，C 使用十四列。行列式和伴随通过完整 Cauchy–Binet 式计算：若
$$
G=\sum_j w_jv_jv_j^T,
$$
则
$$
\det G=\sum_{|I|=d}\left(\prod_{i\in I}w_i\right)\det(v_i:i\in I)^2,
$$
$$
\operatorname{adj}G=
\sum_{|I|=d-1}\left(\prod_{i\in I}w_i\right)c_Ic_I^T,
\tag{4.1}
$$
其中 c_I 是 d×(d−1) 列阵的有符号余子式向量。所有列阵都是明确的整数矩阵。脚本又独立逐项检查
$$
B\,\operatorname{adj}B=(\det B)I,\qquad
C\,\operatorname{adj}C=(\det C)I,
$$
以及最终 𝒫 的对称性。

展开
$$
\mathcal P(z)=\sum_\alpha P_\alpha z^\alpha
$$
后，准确结果为：

- 非零六乘六整数系数矩阵共 7689 个，全部半正定。
- 秩为 1,2,3,4,5,6 的个数依次为 994,276,828,706,720,4165。
- 最终单变量最高次数为 10，总次数最高为 34。
- detB、adjB 的非零 Cauchy–Binet 列组选取数为 303、423；detC、adjC 为 232、84。

系数矩阵的半正性使用完整的精确对称无分数消元。每一步 T/previous 是剩余的真正 Schur 补；选择正对角 pivot 后更新
$$
T'_{ij}=\frac{\mathrm{pivot}\,T_{ij}-T_{ik}T_{kj}}{\mathrm{previous}}.
\tag{4.2}
$$
所有除法均检查余数恰为零，分母和选取的 pivot 严格为正；对称交换行列只是合同。若余块全对角为零，则脚本强制整个余块为零；遇到任何负对角或非零零对角余块即失败。因此这是半正定的严格代数判据，不是浮点 LDL 的近似阈值。

四个变量指数采用独立的 base-32 槽。每次乘法前计算两输入各指数上界并要求相加不超过 13；所有表达式最多含十三个原始多重仿射因子。实际最大输入指数和为 10，故槽间不可能进位。系数与消元全部为 BigInt，且计数、次数、严格锚均有固定断言。完整证明不依赖某组数值权的测试。

## 5. 严格正锚

单项式 (z_1z_2z_3z_4)^4 的系数矩阵，由头边是否相交决定：
$$
(P_{4444})_{I,J}=
\begin{cases}
266240,&I=J,\\
-24064,&|I\cap J|=1,\\
-86016,&I\cap J=\varnothing.
\end{cases}
\tag{5.1}
$$
在六条边的常数方向、三维标准方向、二维修正方向上，其特征值依次为
$$
83968,\qquad352256,\qquad228352.
$$
可直接用四点完全图线图的邻接矩阵核验，也可逐项算六阶特征多项式；三者均正。因此
$$
\mathcal P(z)\succeq(z_1z_2z_3z_4)^4P_{4444}>0.
$$
由 (3.4)，得到严格 H_1H_2^{-1}H_1<H_0。

源基一般非正交，真正 Γ_n 的坐标为 H_0^{-1}H_n，合同后正好给 (1.1)。没有改变先全层取逆、再压 primitive 的约定。

## 6. 固定块的准确归属

定理 1 是六维池固定块。它的价值在于实际短池 L=2<q=4，同时有低端和高端非法状态；§2 已支付这两个约束及真实三维可行参数。它没有由 L≥q 的模板跳过短池。

这里证明系数一，没有声称更小的 3/4 出生因子。也没有用外部优化参数或改变权重来取得正性。

## 7. 整个四异常权 h=2 空间的拼合

原弱池有偶数 M≥0 个单位位，总出生 s=(M+2)/2。按弱池标准正交 Lefschetz 分解，每条弱出生 j 的字符串长度是
$$
L=M-2j.
$$
与四个头张量以后，该分解同时约化 D、D*、完整 F_n 及其全层逆。置相对出生 t=s-j，便有
$$
L=2t-2,\qquad L+4-2t=2.
\tag{7.1}
$$
所有非零 primitive 仅可能来自下面四种相对块。

| 相对出生 t | 弱串长度 L | 固定 primitive 维数 | 已付来源 |
|---|---:|---:|---|
| 1 | 0 | 3 | 四个任意正权的完整 K_1 |
| 2 | 2 | 6 | 本文定理 1 |
| 3 | 4 | 4 | 四头最短倒数第二出生块 |
| 4 | 6 | 1 | 任意头饱和 primitive 线 |

第一行只含四个任意正头权。选一个头权 a_4，整体除以 a_4 后，是三个异常权加一个单位池位，正好属于
[三异常权的完整出生一结果](../results/R271-appendix-three-exceptional-weights-full-birth-one-primitive-gram-bound.md)。
整体缩放 D↦cD 给 Γ_n↦c^(-2n)Γ_n，故相邻系数一比较不变；此行严格成立。

第三行由
[四头四池最短固定块](../results/R239-appendix-four-exceptional-weights-shortest-penultimate-gram-bound.md)
的 4/5 界严格推出系数一。

第四行由
[任意独立头的饱和线 §8](../results/R239-appendix-two-exceptional-weights-full-birth-one-primitive-gram-bound.md)
的真实完整 MP 及正矩表示，给本处 n=1 的 5/6 界，亦严格小于一。

没有 t=0，因为 (7.1) 会要求负长度 L。若 t>4，则 L=2t−2≥8。输入、输出均包含全部头状态，弱删除对角元全部非零，头删除为三角项；该固定删除可逆，故无 primitive。这支付了剩余短串及空块，而非只列有利的四行。

各块的真实串长均为二。完整逆按正交约化块计算后才压 primitive；已有四行的严格正差作有限正交直和，仍严格正定。因此整个 K_s 满足 (1.2)，包括 M=0 的退化池。

本节只处理四异常权模型的 h=2。一般 h 的近端窗口、任意尾权、真实边界修补费用及 ISP 主目标均不由该拼合自动解决。
