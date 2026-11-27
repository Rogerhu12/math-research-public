# R150：全余 W 三生成元的十五行精确原关系表示

会话：Astra-ISP-8542378f-20261127。日期：2026-11-28（Asia/Taipei）。

## 1. 准确结论

在[整个 K7 原排除及全域三生成规则](R150-appendix-unit211-W-entire-K7-complete-original-exclusion-and-global-three-generators.md)的既有余图中，设 $A=A_W$ 只局部化已经支付的权量，$R=A[\lambda]$。物理坐标变换只用已付 $\alpha_t=bcQ/P_{02}$，因而同一六个原式的多项式商可以写作

$$
B=R[x,y]/(E_1,E_{Be},E_{Bo},N_1,N_S,P_S).
\tag{1}
$$

本稿给出 $B$ 的一个**精确的十五行、三列 $R$ 模表示**。它保留全部原六式；不是仅据某个必要行列式构造的外部环境，也不把三个生成元称为自由基底。

此处暂不局部化 $\lambda$、$3-2\lambda$、物理 $D$ 等几何量。需要施加这些原物理条件时，应对同一个代数 (1) 再作对应局部化；不能在任意几何局部化后未经论证把该模仍称为全局有限自由模。

## 2. 三条真实原规则

三条固定均值 $E_1,E_{Be},E_{Bo}$ 的二次头已由整个 K7 排除支付。其真实伴随逆给

$$
q_x=x^2-a_0-a_1x-a_2y,\qquad
q_{xy}=xy-b_0-b_1x-b_2y,
$$

$$
q_y=y^2-c_0-c_1x-c_2y,
\tag{2}
$$

其中全部 $a_i,b_i,c_i$ 属 $R$。它们与三条原均值之间的矩阵变换可逆，只倒置已付权量，故生成同一个原均值理想。

令 $v=(1,x,y)^T$，并定义行作用的两个矩阵

$$
M_x=\begin{pmatrix}
0&1&0\\
a_0&a_1&a_2\\
b_0&b_1&b_2
\end{pmatrix},\qquad
M_y=\begin{pmatrix}
0&0&1\\
b_0&b_1&b_2\\
c_0&c_1&c_2
\end{pmatrix}.
\tag{3}
$$

于是 $xv-M_xv$、$yv-M_yv$ 的每项均为 (2) 的明确组合。此前[十一原行定理](R150-appendix-unit211-W-physical-lambda-eleven-original-rows-two-sextics-and-projection-boundary.md)已实际返回三规则、六条乘法与全部原迹。

写

$$
C=M_xM_y-M_yM_x=
\begin{pmatrix}0\\ C_1\\ C_2\end{pmatrix}.
\tag{4}
$$

第 0 行为零，因为 $M_x$ 的第 0 行取 $M_y$ 的第 1 行，而 $M_y$ 的第 0 行取 $M_x$ 的第 2 行；两者均为 $(b_0,b_1,b_2)$。

对 $N_1,N_S,P_S$ 按 (2) 降低 $x,y$ 总次数，取任意按已刊固定次序完成的原迹余式

$$
N_1\equiv r_Nv,\qquad N_S\equiv r_Sv,\qquad
P_S\equiv r_Pv\pmod{(q_x,q_{xy},q_y)}.
\tag{5}
$$

这里 $r_N,r_S,r_P\in R^3$。不要求重写余式唯一；等式 (5) 的完整原组合已经足够。

## 3. 四个矩阵二次缺陷

直接将 (3) 相乘，逐行得到以下四个身份：

$$
M_x^2-a_0I-a_1M_x-a_2M_y
=\begin{pmatrix}0\\0\\-C_1\end{pmatrix},
\tag{6}
$$

$$
M_xM_y-b_0I-b_1M_x-b_2M_y
=\begin{pmatrix}0\\C_1\\0\end{pmatrix},
\tag{7}
$$

$$
M_yM_x-b_0I-b_1M_x-b_2M_y
=\begin{pmatrix}0\\0\\-C_2\end{pmatrix},
\tag{8}
$$

$$
M_y^2-c_0I-c_1M_x-c_2M_y
=\begin{pmatrix}0\\C_2\\0\end{pmatrix}.
\tag{9}
$$

这些是九个自由系数上的多项式矩阵身份，不使用任何权点采样、几何分母、谱根或原方程的自由基假设。特别是 (6)–(9) 没有要求 $C_1,C_2$ 在自由矩阵空间中分别等于零。

## 4. 十五行给出完整稳定关系模

令五行集合为

$$
G=\{C_1,C_2,r_N,r_S,r_P\}.
$$

定义 $R^3$ 的子模

$$
\mathcal N=
\operatorname{span}_R\{g,\ gM_x,\ gM_y:g\in G\}.
\tag{10}
$$

最多十五行；若某行恰为零或与其它行有关系，仍按 (10) 理解，不强加秩或独立性。

**稳定性。** 对任意 $g\in G$，$gM_x,gM_y$ 已在 (10)。由 (6)–(9)，$gM_x^2,gM_xM_y,gM_yM_x,gM_y^2$ 均是

$$
g,\quad gM_x,\quad gM_y,\quad C_1,\quad C_2
$$

的 $R$ 线性组合。因此

$$
\mathcal NM_x\subseteq\mathcal N,\qquad
\mathcal NM_y\subseteq\mathcal N.
\tag{11}
$$

这一次闭包已经足够，不需要无限地追加所有乘积行，也没有把“前几轮没有找到新行”当作稳定性证据。

于是两个矩阵在 $V=R^3/\mathcal N$ 上诱导真正的线性作用。由 (4)，它们在 $V$ 上交换；由 (6)–(9)，它们在 $V$ 上满足三条 (2) 的算子关系。这些结论是因为全部缺陷行落入 $\mathcal N$，不是在原六个或三个无关系生成元上强行要求矩阵交换。

## 5. 与完整六式商的双侧同构

记 $e_0,e_1,e_2$ 为三个标准行向量。按 (3) 有

$$
e_0M_x=e_1,\qquad e_0M_y=e_2.
\tag{12}
$$

因此 $V$ 作为由 $x,y$ 的诱导作用生成的模，以 $e_0$ 为循环元。定义

$$
\psi:R[x,y]\longrightarrow V,\qquad
p\longmapsto e_0p(M_x,M_y).
\tag{13}
$$

此处 $p(M_x,M_y)$ 在 $V$ 上有意义，因为诱导作用已由 (4)、(11) 证明交换。式 (6)–(9) 保证三个 $q$ 作用为零。式 (5) 又给

$$
\psi(N_1)=r_N,\quad\psi(N_S)=r_S,\quad\psi(P_S)=r_P
\quad\text{in }V,
$$

而三行都属 $\mathcal N$。所以 (13) 经过 (1) 得到满射

$$
\bar\psi:B\longrightarrow V.
\tag{14}
$$

反方向定义

$$
\phi:R^3\longrightarrow B,\qquad
(r_0,r_1,r_2)\longmapsto r_0+r_1x+r_2y.
\tag{15}
$$

由真实乘法身份，$\phi(rM_x)=x\phi(r)$、$\phi(rM_y)=y\phi(r)$。原多项式商中的 $x,y$ 交换，故 $C_1,C_2$ 在 (15) 下为零；(5) 给 $r_N,r_S,r_P$ 也为零。因此 (10) 的全部十五行均在 $\ker\phi$，(15) 下降成

$$
\bar\phi:V\longrightarrow B.
\tag{16}
$$

式 (12) 说明两个映射在 $1,x,y$ 以及三个标准生成元上互为逆；两边均由这些元素生成。故

$$
B\ \cong\ R^3/\mathcal N.
\tag{17}
$$

这同时证明 (10) 没有漏掉所需的任意高次关系，不只是构造了从原商到某个必要环境的一向映射。

## 6. 原迹、已有十一行与真正新增输入

每个 $g\in G$ 都具有同一六原式的完整迹

$$
gv=\tau_g F_6,\qquad F_6=(E_1,E_{Be},E_{Bo},N_1,N_S,P_S)^T.
$$

若 $xv-M_xv=E_xF_6$，则完整同点乘法公式为

$$
(gM_x)v=(x\tau_g-gE_x)F_6,
\tag{18}
$$

对 $y$ 同理。这明确给出 (10) 每一行的原理想来源。

此前实际十一行已经包含五行 $G$，以及 $C_1,C_2,r_N$ 分别乘 $M_x,M_y$ 的六行。新精确表示只补

$$
r_SM_x,\quad r_SM_y,\quad r_PM_x,\quad r_PM_y.
\tag{19}
$$

它们不是一个新未经解释的矩阵自由条件，而是原 $xN_S,yN_S,xP_S,yP_S$ 的真实同点返回。按 (18) 即得完整原迹。固定可逆的已付权比例归一不改变 $\mathcal N$；不能剥掉未付的行内容。

本稿没有运行新的十五行展开或新的余子式、结果式、Gaussian 门，也没有重跑已冻结的十二阶 Sylvester 计算。它提供一个可直接用于后续原低度计算的精确表示定义。

## 7. 与全域首一 λ 六次式的组合

[同一原均值理想的首一物理 λ 六次式](R150-appendix-unit211-W-global-original-physical-lambda-monic-six.md)给出

$$
\chi_\lambda(\lambda)\in I_4\subset I_6,\qquad
\chi_\lambda\in A[\lambda]\text{ 首一六次}.
$$

因此可先在明确自由六维环境

$$
S=A[\lambda]/(\chi_\lambda)
$$

上解释 (17)，再取十五行的像。该环境里的三列原关系仍须施加；不能因为环境自由而称原最终商自由。

由于 $\chi_\lambda$ 原本就在 (1) 的理想中，换成 $S^3/\overline{\mathcal N}$ 不增加任何假条件。作为 $A$ 模得到的“至多 18 个环境生成元”只是计算环境上界；此前原六生成定理已给更强的至多 6 个生成元，本稿不把较弱的 18 重新登记为研究进展。

全部未付权因子、$\lambda$ 首项和内容零支都继续保留；原物理局部化与完整个别 N/P 条件仍要按原图处理。本表示本身不宣称整个 W 排空。
