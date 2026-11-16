# R472：真实二三阶前缀复位、多个相同保护芽与不可删除的新段 ruling

日期：2026-11-16。**完整纸面证明；没有执行新的符号程序、原根恢复、profile 求积、秩、人工检查或数值研究。**

本稿继续 [R469](R469-global-gauge-locking-and-real-prefix-obstructions-between-rational-germs.md) 的真实相对前缀门。结论不止是能够指定若干二阶矩阵：原 R70 矩阵桥加原完整第三 prototypes，确实能在同一个有限实际词中同时复位二阶与完整第三历史。具体地，任意一个首末同常数 scalar germ 的固定模板 $G$，可以接一条真实正时长返回桥 $B$，使
$$
A_{GB}=0,\qquad T_{GB}=0.
$$
这个复位单元在任何传入二阶、三阶历史下都返回原值。因此，把有限多个 $GB$ 放在原 $G$ 之前，会产生有限多个具有**完全相同真实 incoming 数据**的保护芽。条件使用 R468 的同一个 $J_{\rm aff}$ 实际截面和 R467 的 vertical 后，同一个 $w_\theta,\chi_\theta$ 可以支付全路径第四 period，并同时支付所有这些相同、同向的标记芽；每个新增完整第四基准均进入同一次实际成本目标。

另一方面，复位桥不会从全段 ruling 问题中消失。一个包含 $k=\kappa\ne0$ 保护段的整 $M=0$ 复位单元，不可能始终保持同一个 $\omega$。原八矩甚至给出它必须承担的准确恒等式
$$
\int kh(\omega-\omega_c)\,ds
=\int k^2\,ds
=L+\int(h_s/h)^2\,ds>0.
$$
所以新词必经原有理恒 $\omega$ 芽以外的真实状态段。本稿给出这些段的完整传入历史 ruling 公式、相同 prototype 重复时的准确二次多项式，以及一个不能用倒行取消的正成本结论。没有把已付全 period、多个保护芽或有限成本截面说成全部 $s$ 段已经完成。

以下实际成本接线仍以**同一初选库、同一共同窗口和 R468 的比例条件**为前提。本文不预判当前四个新 self 结果所决定的该比例关系。

## 1. 固定原始规范：三种历史与完整算子

固定原共同物理区间 $I=[\ell,r]$、全部右原函数及左右 collars。所有路径满足
$$
h>0,\qquad \omega_s=\frac{k_s}{2h},\qquad
F_s=F\Omega(k),\qquad x+\omega>0.
\tag{1}
$$
没有为不同段重选物理 $x$、profile 或右锚。实际 scalar 常态记为
$S=(h,k,\omega)$；frame 端值另外指定，空间末位移不预先指定。

对实际块 $B$，沿用 [R83](R83-true-fourth-transfer-and-zero-lower-history-variations.md)：
$$
A_B=\Phi_{M_B},\qquad T_B(a;D),\qquad V_B(F,\phi).
\tag{2}
$$
$A_B$ 是原 E8 完整二次算子，$T_B$ 保外槽及对称内槽，$V_B$ 是由零传入二、三阶 scalar 历史按原 forcing 得到的整个第四周期函数。不是只取对角，也不是只取 $\pi$、左二次 self 或某一个 flux。

写
$$
(A\circ C)(a;g,j)=A(a,C(g,j)),\qquad A^2=A\circ A.
\tag{3}
$$
这里的乘法只表示这个明确的三槽复合，不要求它是某个未证明的抽象群表示。

固定第一圆和目标
$$
\phi_\theta=f\cos\theta+g\sin\theta,\qquad
F=f^2,\qquad D_\theta=F-\phi_\theta^2.
\tag{4}
$$
令进入块的第二、第三、第四 scalar 历史分别为 $a,b,c$。原完整传递是
$$
\begin{aligned}
a'={}&a+A_BD_\theta,\\
b'={}&b-2T_B(\phi_\theta;D_\theta)+2A_B(\phi_\theta,a),\\
c'={}&c+V_B+2T_B(a;D_\theta)
 -4T_B(\phi_\theta;\phi_\theta,a)\\
&-A_B(a,a)+2A_B(\phi_\theta,b).
\end{aligned}
\tag{5}
$$
所有 profile 都保持原右 collar；有真实左尾时先保留，不能为应用此式把它改成单包紧函数。

本文把“先走 $B_1$、再走 $B_2$”写为 $B_1B_2$。R83 的完整组合式于是为
$$
\begin{aligned}
A_{B_1B_2}&=A_1+A_2,\\
T_{B_1B_2}&=T_1+T_2-A_2\circ A_1,
\end{aligned}
\tag{6}
$$
$$
\begin{aligned}
V_{B_1B_2}={}&V_1+V_2
+2T_2(A_1D_\theta;D_\theta)
-4T_2(\phi_\theta;\phi_\theta,A_1D_\theta)\\
&-A_2(A_1D_\theta,A_1D_\theta)
-4A_2(\phi_\theta,T_1(\phi_\theta;D_\theta)).
\end{aligned}
\tag{7}
$$
下文每一次“复位”“插入”和“相加”均使用(5)–(7)，不假定未付的第四逆路径。

## 2. 任意指定二阶量时，完整第三仿射类仍可准确识别

沿用 [R80](R80-complete-third-affine-class-and-P1-endpoint-obstruction.md) 的真实有限维第三空间
$$
W=W_{71}+V_3+W_1.
\tag{8}
$$
$W_{71}$ 是原 E8 完整三槽交换子跨度；$V_3$ 与 $W_1$ 分别是 R77、R79 已有真实有限控制的局部权三和闭水平权一空间。不把三者的生成列数相加当维数。

R80 固定常数 scalar 端口 $S_-,S_+$，由局部第三密度得到端点类
$T_{\rm end}(S_-,S_+)$，只在模 $W$ 下唯一。本节将其原 $M=0$ 结论延到任意固定 $A$。

**定理 1：任意 $A$ 的完整第三类。** 在 R70/R80 原共同窗口与有限控制词的范围内，指定常数 scalar/frame 端口及任意有限 $A\in E_8$，其完整实际第三响应集合准确是
$$
\boxed{
\operatorname{Reach}_3(A;S_-,S_+;F_-,F_+)
=T_{\rm end}(S_-,S_+)-\frac12A^2+W.
}
\tag{9}
$$
有界目标参数族可以保持固定有限词型和 $C^1$ 依赖。

**必要性。** 令
$A_s=\Phi_{\mathsf m(s)}$，其中 $\mathsf m_s=M_{\rm raw}(s)$ 且
$A_0=0$。R73 的完整第三式为
$$
T_B=-\int_0^L A_s'\circ A_s\,ds+\int_0^L C_s\,ds.
\tag{10}
$$
这是原真实历史，不在子段重置。由
$(A_s^2)'=A_s'\circ A_s+A_s\circ A_s'$，
$$
-\int_0^L A_s'\circ A_s+\frac12A_L^2
=\frac12\int_0^L(A_s\circ A_s'-A_s'\circ A_s)\,ds
\in W_{71}.
\tag{11}
$$
不需要 $A_L=0$。

R80 对局部项的分解
$$
C_s=D_s(P_{\rm acc}+P_h)+C_{3,\rm rem}+k_sR
\tag{12}
$$
不使用总矩阵零。常值端芽给 $P_{\rm acc}$ 两端零；其余两部分在模
$V_3+W_1$ 后恰留下同一个 $T_{\rm end}$。因此(10)–(12)给
$T_B+\frac12A_B^2\in T_{\rm end}+W$。若原记号中的第三 ambient 空间只含零矩路径，取它与有限个 $E_8\circ E_8$ 的跨度即可；不改变 $W$ 或任何实际函数身份。

**充分性。** R70 先构造一条真实桥 $B_0$，准确给指定的 $A$ 和两端 scalar/frame。它的完整第三值 $T_0$ 不猜、不删除。由必要性，任意(9)中的目标 $T_*$ 满足
$T_*-T_0\in W$。在右端常值 germ 接 R71/R77/R79 原完整三阶控制环，实现这个差。每个插入环 $A=0$、frame 恒等、scalar 返回原态，故(6)中的交叉项为零，完整第三严格相加。它们的第四成本仍全部保留。

有限实际生成表给局部 $C^1$ 右逆；对一个固定紧目标集，使用原有限重复及有限覆盖，把词型与各整数固定。整个构造使用正时长实际块，不使用负路径。证毕。

式(9)既给可达性，也保留限制：固定 $A$ 后不能任意指定整个三槽空间，只能指定这个准确仿射类。不同 scalar 端口的 $T_{\rm end}$ 仍须保留；在非恒定端点还会有(12)的原加速度端项，不能把那里当作新的常数 collar。

## 3. 有限标记前缀的二、三阶同时归一

设一条已走前缀的完整二、三阶量为 $(A_-,T_-)$。希望经过一座连接桥后变成 $(A_+,T_+)$。由(6)，桥必须满足
$$
a=A_+-A_-,\qquad
T_B=T_+-T_-+a\circ A_-.
\tag{13}
$$
因此定理 1 给准确的必要充分条件
$$
T_+-T_-+a\circ A_-+\frac12a^2-T_{\rm end}
\in W.
\tag{14}
$$

定义完整修正第三类
$$
\Theta(A,T)=T+\frac12A^2.
\tag{15}
$$
双线性展开显示(14)左边与
$\Theta(A_+,T_+)-\Theta(A_-,T_-)-T_{\rm end}$
只差
$\frac12(A_+\circ A_--A_-\circ A_+)\in W$。所以(14)也准确等价于
$$
\boxed{
[\Theta(A_+,T_+)]-[\Theta(A_-,T_-)]
=[T_{\rm end}]
\quad\text{于 }E_3^{\rm ext}/W.
}
\tag{16}
$$

特别，若若干模板的入口都是同一个常值 scalar 状态 $S_c$，取一个实际参考前缀 $(A_*,T_*)$ 到达此状态。任何别的实际前缀到同一状态，在(15)的商类都相同；端点势只依固定初、末 scalar 状态。故可依次用(13)构造真实连接桥，使**每个指定入口**都准确具有 $(A_*,T_*)$，frame 也归一到指定参考值。前面已经完成的模板和桥只决定下一座桥的真实有限目标，不造成新的代数相容条件。最后一座同类桥可将全体二阶量置零，并给一个在(9)允许类内的指定完整第三量，例如原 hook 方向的预定倍数。

这项逐段构造已经支付完整外槽第三，而非只支付 $M$ 或三阶对角。所有新桥的时长、位置位移和第四基准仍在真实词中。它不说不同模板的内部场相同：若模板自身不同，入口相同仍不替代各自的 ruling 方程；若标记中心不是常数端点，也不能自由删掉从模板入口到中心的第三端项。

对完全相同的固定模板，则可采用下一节更强而更简单的复位单元。

## 4. 任意固定模板都有真实二三阶复位补块

取一个固定真实模板 $G$，首末 scalar 状态均为同一个常态 $S_c$，两端有开常值 collar。其末 frame 不必等于初 frame。记
$$
A_G=A,\qquad T_G=T,\qquad V_G=V.
\tag{17}
$$
模板可以含原保护芽
$$
h=H(1+\varepsilon\sigma^2),\qquad
k=\kappa\ne0,\qquad\omega=0.
\tag{18}
$$
例如先在一个固定开子区间取(18)，再保持 $k=\kappa,\omega=0$，把正函数 $h$ 光滑接回相同的常数端值。这满足(1)，不要求模板自己 frame 闭合。

**定理 2：真实复位单元。** 存在一条从 $G$ 末 frame 返回初 frame、scalar 首末均为 $S_c$ 的真实有限桥 $B$，使
$$
\boxed{
A_B=-A,\qquad T_B=-T-A^2,\qquad
A_{GB}=T_{GB}=0.
}
\tag{19}
$$
对固定紧模板参数族，可取有限词型和 $C^1$ 依赖。

**证明。** 相同 scalar 端点给 $T_{\rm end}=0$。定理 1 先对实际 $G$ 给
$T+\frac12A^2\in W$。所要求桥的修正第三量为
$$
(-T-A^2)+\frac12(-A)^2
=-\left(T+\frac12A^2\right)\in W.
\tag{20}
$$
所以原 R70 矩阵桥和原 $W$ 第三环实际实现(19)前两式，包括指定 frame 返回。再代入(6)，
$T+(-T-A^2)-(-A)\circ A=0$。没有把某个形式负号解释成负时间。证毕。

记实际复位单元
$$
P=GB.
$$
由(5)，**对任意原允许的完整传入历史**，
$$
\boxed{(a,b,c)\longmapsto(a,b,c+V_P).}
\tag{21}
$$
第四基准准确为
$$
\begin{aligned}
V_P={}&V_G+V_B
+2T_B(AD_\theta;D_\theta)
-4T_B(\phi_\theta;\phi_\theta,AD_\theta)\\
&-A_B(AD_\theta,AD_\theta)
-4A_B(\phi_\theta,T(\phi_\theta;D_\theta)).
\end{aligned}
\tag{22}
$$
式(22)全部保留。它一般不是 $0$，也不是某个完整响应列或 $V_G-V_G$。$V_B$ 包含矩阵桥和全部补第三环的真实成本。

$P$ 回到相同 scalar/frame，且整 $M=T=0$，因此 $V_P$ 是原实际成本半群中的一个成员，属于原有限线性空间 $U$。相反，构造中某个尚未闭合的裸桥成本不因此单独属于 $U$；对它不能擅自使用只定义在 $U$ 上的成本观测。

## 5. 多个保护芽共用真实 incoming，而非共用一个虚拟零初值

在原 R467 背景的同一个实际位置类型上固定上述模板 $G$。在它之前插入有限个复位单元，得到
$$
P^qG=(GB)^qG,\qquad q\in\mathbb N.
\tag{23}
$$
每个完成的 $P$ 回到同一个 scalar/frame。故这里 $q+1$ 个 $G$ 的起始 frame、scalar 和真实传入 $(a,b)$ 完全相同；仅空间起点可能有平移，而物理 ruling 配对不依赖整体空间平移。

更强地，设原 $G$ 入口之前的完整前缀为 $(A_{\rm pre},T_{\rm pre})$，原全局二阶、三阶规范为 $w_\theta,\chi_\theta$。由于原第三场写作加 $Y_{\chi_\theta}$，在(5)的符号中初始第三 scalar 是 $-\chi_\theta$。因此所有这些入口的真实数据均为
$$
\boxed{
\begin{aligned}
a_\theta={}&w_\theta+A_{\rm pre}D_\theta,\\
b_\theta={}&-\chi_\theta-2T_{\rm pre}(\phi_\theta;D_\theta)
+2A_{\rm pre}(\phi_\theta,w_\theta).
\end{aligned}}
\tag{24}
$$
不是只说它们的二阶矩阵相同，也不是在每个 $G$ 入口重新设第三为零。

在每个模板的同一个局部位置，局部 scalar 函数、全部导数及从入口开始的真实恢复完全相同。R83 的原向量场身份
$$
Z_2=Z_G(D_\theta)-Y_{a_\theta},\qquad
Z_3=W_G(\phi_\theta,D_\theta)
+2Z_G(\phi_\theta,a_\theta)-Y_{b_\theta}
\tag{25}
$$
便给全部 matched 场相同，或在共同环境刚体转动下相同。故其完整第四 ruling 逐点相同。

这证明：**若同一个 $(w_\theta,\chi_\theta)$ 支付其中一个标记保护芽，它同时支付(23)的所有相同、同向标记芽。** 它还使 R469 的全部相对前缀最高门准确为零；第三传入偶部也一并匹配，没有再留下每个芽各选三矩的自由。

此结论不外推到任意不同的 rational germ。只把 $M$ 归一并不使不同模板的完整 canonical ruling 相同。原四块闭合中另外出现的反向或异型段，必须使用其真实拉回与 incoming，不能仅凭“也是一个芽”列入上述相同副本。

## 6. 全部新增第四基准接入同一个实际成本截面

现在明确与 R468/R467 的连接条件。一次固定同一初选 profile 库、同一个
$$
J=J_{\rm aff},
$$
全部 cap、角色、宽度与右锚，并采用 [R468](R468-real-height-pulse-fills-affine-residual-and-completes-actual-enhanced-cost-control.md) 对同一增强映射已经证明的分支：

- R466 的完整闭锥条件 $h\in\operatorname{span}\{y\}$ 成立；
- 全部近一变换、真实矩阵桥、第三 prototypes、复位桥及其参数包络已经从起点纳入同一个合法物理窗口；
- 采用 R467 原加强库和固定非零 $\tau$，包括同一 $M_3\ne0$、二十目标及外宏包装。

这里 $h,y$ 指 R466 的两个共同 self 商类，不是几何高度。本文不把 $y\ne0$ 或两列各自非成员当作比例关系已付。

在这些条件下，R468 提供同一 $J$ 的真实有限 $C^1$ 截面；R467 的原 $K_P=\mathcal B_P\mathfrak H$ vertical 在其核中仍满足
$$
\widetilde d(K_P)=-\eta_P/\tau\ne0.
\tag{26}
$$
故完整联合观测 $(J,\widetilde d)$ 具有同一个实际截面。不是把两个独立 signed 解相加。

将(23)连同全部原背景与闭合桥一次固定。单个背景体中，每个完成的复位单元按(21)增加完整 $V_P$；原闭合按 R467 的同一个修改后单体执行。把**整条实际闭合背景**的所有这些项统一记为
$V_{\rm base}^{(q)}$。它已包含复位桥、第三补偿环、实际重复、原桥和各个闭合位置的准确贡献；不将裸桥单独套成本商，也不把它们归入待删除误差。

按原 R467 的 Klein 规范，
$$
V_{\rm final}=V_{\rm base}^{(q)}+4V_{\rm ctrl}.
\tag{27}
$$
四倍只在这套原规范中使用。完整 $M=0$、scalar/frame 闭合使
$V_{\rm base}^{(q)}\in U$：也可由其真倒行给
$2V_{\rm base}^{(q)}$ 是实际零二、三阶成本来识别。空间位移由同一个修改后单体的原四块组装支付，不要求每座 $B$ 或 $P$ 单独零位移。

所有成本控制块均整 $M=T=0$，在标记芽之外完整插入。由(21)，它们保持(24)的整个 incoming。尤其被选保护芽中心的真实
$X_*=\Phi_{\mathsf m_*}$ 在目标截面中固定，最终第三系数仍是原 $\tau$。因此在同一联合截面中取
$$
\boxed{
J(V_{\rm ctrl})=-\frac14J(V_{\rm base}^{(q)}),\qquad
\widetilde d(V_{\rm ctrl})
=-\frac14\{\widetilde d(V_{\rm base}^{(q)})+d_f(X_*)\}.
}
\tag{28}
$$
这准确支付最终 $J=0$ 和最高第一行。最高第二行、两个真 period range、其余九行与三合法矩，均按 R467/R464 的同一个规范构造支付。

**定理 3：条件性的多个相同保护芽实际结论。** 在本节同点条件下，对任意预先固定的有限 $q$，存在原有限实际背景加控制词，并有同一个相位光滑、保种子的
$(w_\theta,\chi_\theta)$，同时支付：

1. 完整固定-$\tau$ 的低阶结构和全路径第四 period；
2. 整个 $J_{\rm aff}$ 与原 highest-$d$ 成本目标；
3. (23)中全部 $q+1$ 个相同、同向标记保护芽的完整十三行与 ruling。

证明由(19)–(28)及 R467 的同一规范得到。特别，新增 $qV_P$ 和控制 prototypes 乘真实整数的基准一直在(27)(28)内；没有免费复制，也没有把桥成本改名后省去。

定理不包括其余桥内部、其他方向副本和成本控制块内部的 ruling。即使这些块的整 $A=T=0$，(21)也只说明**离开整块时**的低阶历史复位及第四周期加法，不说明块内场或 forcing 为零。

## 7. 每座新增桥内，真实第四 ruling 的完整传入公式

本节不用“成本已付”替代局部方程。固定一个真实块 $B$，以它自己的入口零二、三阶历史定义
$Z_B(D_\theta)$、$W_B(\phi_\theta,D_\theta)$ 和 canonical ruling
$\mathscr K^0_{B,\theta}(s)$。所有这些仍是原同锚恢复，不是另改整条路径的实际入值。

令 $\mathcal E_s(v,z)$ 是原 physical ruling 配对
$$
\mathcal E_s(v,z)=\int (Y_v)_u\cdot(Y_z)_u\,du.
$$
若一槽有真实左尾，先按这个实际定义保留；只有原端项确已支付时，才使用
$\mathcal E_s(v,z)=\mathbf w(s)\cdot\mathbf I(v,z)$ 的简式。记
$$
\begin{aligned}
\mathcal B_{B,\theta}(a)(s)
={}&2\int (Z_B(D_\theta))_u\cdot(Y_a)_u\,du\\
&-4\int(Y_{\phi_\theta})_u\cdot(Z_B(\phi_\theta,a))_u\,du .
\end{aligned}
$$
由(25)直接代入完整 forcing
$-H(Z_2,Z_2)-2H(Y_{\phi_\theta},Z_3)$，得到
$$
\boxed{
\mathscr K_{B,\theta}^{(a,b)}
=\mathscr K^0_{B,\theta}
+\mathcal B_{B,\theta}(a)
-\mathcal E_s(a,a)+2\mathcal E_s(\phi_\theta,b).
}
\tag{29}
$$
这里 $\mathcal B_{B,\theta}$ 对 $a$ 严格线性；平方项和完整第三入值仍在(29)。令 $a=w_\theta,b=-\chi_\theta$ 即回到 R184 的原号。

特别，对一个整 $A_B=T_B=0$ 的块，(21)并不能推出(29)为零。$A_B,T_B$ 是完整积分算子，(29)是每一个内部 $s$ 的真实函数。两个 $M=T=0$ 块有相同的 $J(V)$，也没有因此得到相同的(29)。

在固定全局 $w_\theta,\chi_\theta$ 时，插入完成的复位块不改变它之后原有段的低阶场；但是为支付新增 $V_P$ 而重新求得的 $w_\theta,\chi_\theta$ 一般会变化。因此不能声称“插入后原所有 ruling 自动保持”。定理 3 所保持的是原式保证的相同保护芽及所列全周期目标，其余段仍必须在最终选定的同一个规范下消费(29)。

## 8. 真实重复 prototype 的 ruling 只有二次重复依赖，但这些系数必须保留

同一个实际块 $B$ 回到相同 scalar/frame，允许连续重复。不同副本的环境刚体位置不影响下列配对。固定第一次入口 $(a_0,b_0)$，定义
$$
v=A_BD_\theta,\qquad
r_\theta=-2T_B(\phi_\theta;D_\theta)+2A_B(\phi_\theta,a_0),\qquad
c_\theta=A_B(\phi_\theta,v).
\tag{30}
$$
由(5)逐次相加，完成 $j$ 个副本后的真实输入准确是
$$
\boxed{
a_j=a_0+jv,\qquad
b_j=b_0+jr_\theta+j(j-1)c_\theta.
}
\tag{31}
$$
这里 $r_\theta,c_\theta$ 是 profiles，不是几何右端点或第四成本。

将(31)代入(29)，在每个副本的同一个局部位置有完整函数身份
$$
\boxed{
\mathscr K_j(s,\theta)
=\mathscr K_0(s,\theta)
+j\,\mathscr C_1(s,\theta)+j^2\,\mathscr C_2(s,\theta),
}
\tag{32}
$$
其中
$$
\begin{aligned}
\mathscr K_0&=\mathscr K^{(a_0,b_0)}_{B,\theta},\\
\mathscr C_1&=\mathcal B_{B,\theta}(v)
-2\mathcal E_s(a_0,v)
+2\mathcal E_s(\phi_\theta,r_\theta-c_\theta),\\
\mathscr C_2&=-\mathcal E_s(v,v)
+2\mathcal E_s(\phi_\theta,c_\theta).
\end{aligned}
\tag{33}
$$
这是对真正整数重复号的恒等式，不是近似或一阶微分主项；原 profile 非局部尾和全部第三 history 已经在这些 profiles 与配对内。

因此，当实际词含至少三个连续副本时，全部副本 ruling 恒零，等价于这三个完整函数
$\mathscr K_0,\mathscr C_1,\mathscr C_2$ 都为零。证明只是在任意固定 $(s,\theta)$ 对二次多项式取三个不同整数，随后恢复全函数身份。对一个或两个副本只要求其实际出现的相应方程，不能多加未出现的三行。

两个特例具有直接含义。

**第三 prototype。** 若 $A_B=0$，则
$$
\mathscr C_2=0,\qquad
\mathscr C_1=-4\mathcal E_s\{\phi_\theta,T_B(\phi_\theta;D_\theta)\}.
\tag{34}
$$
所以一个 $M=0$、$T_B\ne0$ 的 prototype 乘 $n$，其内部第三输入仍可能逐副本变化。若(34)在所选真实圆上不恒零，两个相同副本不可能靠一个共同第三 Gram 初值同时清 ruling。反之，若原 profile 身份使(34)为零，就按该真实身份消去；不能从 $T_B\ne0$ 自行宣它非零，也不能从最终第三总量固定自行宣它零。

**整复位单元。** 若 $A_B=T_B=0$，则
$$
\mathscr C_1=\mathscr C_2=0.
\tag{35}
$$
所有副本的 ruling 相同，但其共同值 $\mathscr K_0$ 仍待支付。故增加(23)中的相同复位单元不会增加新的 matched 局部方程类型，却会增加真实正时长与完整第四基准。

(32)也适用于原 R468/R467 的真实有限重复，只要按其实际重复块取 $A_B,T_B$。不能把比较词、矩阵桥或第三 prototype 的 $O(1)$ ruling 当作相对于 $n$ 自动消失。对于“必须准确为零”的 range 条件，任何有限非零系数都不能靠选大 $n$ 删除。

## 9. 复位单元的完整成本严格为正，真倒行不能取负

[R406 第 7 节](R406-complete-weight-zero-natural-fluxes-and-canonical-joint-obstruction.md) 从原 R196 完整局部化及八矩给：对真实正时长、同常数 scalar germ、frame 闭合、整 $M=0$ 的 canonical 成本，
$$
\boxed{
\lambda_+(V_B)=\int_B k^2\,ds
=L_B+\int_B(h_s/h)^2\,ds>0.
}
\tag{36}
$$
不要求整 $T=0$。这是完整实际成本恒等式，包含所有 history 和原 $\Gamma M$ 端规范；不是由某个 static normal 系数的号猜出的成本性质。

定理 2 的 $P$ 正好满足这些前提，所以
$$
\lambda_+(V_P)>0,\qquad V_P\ne0
\quad\text{作为完整 universal 成本。}
\tag{37}
$$
尤其，不能把复位桥 $B$ 称为第四逆。整 $M=0$ 的同 $k$ 真倒行满足原 R83
$$
A_{P^R}=0,\qquad T_{P^R}=-T_P=0,\qquad V_{P^R}=+V_P.
\tag{38}
$$
于是 $PP^R$ 给 $2V_P$，不会取消它。任意非空有限串联的这种正时长零矩闭块，也不能实现完整成本 $-V_P$。

这不反驳(28)：R468/R467 指定的是同一个有限 $J_{\rm aff}$ 及 highest-$d$ 观测，不是任意指定整个 $V\in U$。更不把(37)直接升级为所选固定圆、加二阶规范后的 fourth range 不可能。原正字符经过 universal 自然函数下降，与它是否经过当前固定库的有限 $J_{\rm aff}$ 下降，是两个已经明确区别的问题。

## 10. 一个不能回避的新段：恒 $\omega$ 的整零矩字只能有 $k=0$

[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md) 的两个原逐点坐标为
$$
p_1=-k(h\omega-k)=k^2-kh\omega,\qquad p_2=-kh/2.
\tag{39}
$$
对整 $M_B=0$，两个坐标的积分均为零。因此对任意固定参考常数 $\omega_c$，
$$
\boxed{
\int_B kh(\omega-\omega_c)\,ds=\int_B k^2\,ds.
}
\tag{40}
$$
若 $\omega\equiv\omega_c$，(40)迫 $k\equiv0$。

特别，$P=GB$ 包含(18)中一段非空 $k=\kappa\ne0$，所以
$$
\omega\not\equiv0\quad\text{于整个 }P.
\tag{41}
$$
由于(1)，真实返回桥中必有新的 $\omega$ 变化段，也有 $k_s\ne0$ 的开子段。对本稿同常端、frame 闭合的正时长复位单元，即使不先指定 $\kappa\ne0$，(36)(40)也排除整个 $\omega$ 恒定；这里只用保护段便已得到这个必要性。它不能只由原恒 $\omega=0$ 的 rational 模板及同类常态段拼成。更一般，保持任意一个共同常数 $\omega_c$ 也不能完成此复位。

结合(36)，还得到一个保留实际量的必要账：
$$
\boxed{
\int_P kh(\omega-\omega_c)\,ds
=L_P+\int_P(h_s/h)^2\,ds>0,
}
\tag{42}
$$
因而
$$
\|\omega-\omega_c\|_\infty\int_P|kh|\,ds
\ge L_P+\int_P(h_s/h)^2\,ds.
\tag{43}
$$
没有据此声称任意预给幅度或时长预算可实现。它恰说明：R70/R80 允许的有限返回桥确实使用了额外状态范围，不能把这部分隐藏成保持原芽形式的“中性连接”。

式(41)–(43)不证明这些新段的 ruling 必非零；它们严格否定的是把所有新段都算作已付相同 rational 芽的省略法。

## 11. 同一个规范的剩余自由度，不能给每座桥重新分配

最终实际词选定后，R469 的锁定结论仍原样适用。已付一个保护芽与全 period 的规范记为
$(\bar w_\theta,\bar\chi_\theta)$。任何允许的再改动必须满足
$$
L_f\eta_\theta=0,\qquad C_\theta\beta_\theta=0,
\tag{44}
$$
其中原 period 核分解为
$$
\eta_\theta=\sum_i\beta_{i,\theta}u_i
+\sum_i\beta_{n+i,\theta}\chi_i+\eta_{\rm gap,\theta}.
\tag{45}
$$
$C_\theta$ 是原十三行矩阵；这里不宣称十三是秩。

原已付芽的三权独立，故保持它会唯一决定第三 Gram 矩改变量。保全部平方项后，整条路径 ruling 的准确增量为
$$
\delta\mathscr K_\theta
=\mathcal P_*\mathcal B_\theta(\eta_\theta).
\tag{46}
$$
所以不能在每个返回桥各加一套第三三矩。所有桥、成本控制块、原背景段，必须共用同一个 $\beta_\theta$ 和(46)所迫的第三矩。

这里两类“平台”必须分开。

1. 在所有实际活动包上恒零的真正间隙函数满足
   $\mathcal B_\theta(\eta_{\rm gap})(s)=0$，对**全部真实 $s$**成立。新返回桥经过不同 $\omega$ 不会使这个不可见空间突然变成新的自由控制。原二次尾的 $I_2$ 两项准确相消，不是把尾删除。
2. 在某包上恒为 $1$ 的原平台基 $\chi_i$ 并不盲。令
   $c_i=a_i\cos\theta+b_i\sin\theta$、$d_i=a_i^2-c_i^2$、$\mu_i=\mathbf I(u_i,u_i)$，R469 的完整响应仍为
   $$
   \mathcal B_\theta(\chi_i)
   =-\frac{d_i}{2}\mathbf w'\cdot\mu_i
   +2\mathbf w\cdot
   \{-d_i\ell_{\mathsf A_s}(\mu_i)
       +c_i^2q_{\mathsf A_s}(\mu_i)\}.
   \tag{47}
   $$
   其中 $\mathsf A_s$ 是**最终整词**的真实八维累计，$\ell,q$ 为 R469 原左右二次尾表；$\mu_{i,2}$ 保含 $2(u_i')^2$。新桥上这些量会改变，不能沿用原芽处的常值代替。

于是新增返回桥的待付对象已经明确：在同一个最终词上，将(29)及必要的(32)(33)与所有原段一起，代入 R469 的同一个(44)–(47)联合方程。它不再只是“还缺一些二阶前缀”；二阶、三阶前缀可以真实归一，剩下的是这些明确的完整局部函数。

对一套固定有限词，按实际出现的有限块类型保存零入值场和 $A_s,T_s$，重复段再用(32)即可，不必为每个复制号发明一个新未知规范。这是有限的原式接线；没有把有限类型数、42 个生成元或三项重复多项式系数称为已证明的满秩。

## 12. 本稿已闭合的构造与仍准确未付的部分

本稿已经证明三件此前相互不能替代的事：

- 对任意指定二阶 $A$，原完整第三的实际可达类是(9)，所以可真实同时指定有限个相容的二、三阶入口；不是仅 R70 的矩阵层。
- 每个同常端固定模板都能补成整 $A=T=0$ 的实际复位单元。有限复制使全部相同标记芽共享完整 incoming；条件调用同一 R468/R467 截面时，所有新增 $V$ 基准统一进入(28)，同一个规范支付全 period 和这些芽。
- 返回桥必须经过新的非恒 $\omega$ 状态段，其 canonical 完整成本严格正，倒行同号；这些段的 ruling 由(29)–(35)准确给出，不能从整块复位或成本零观测推掉。

因此，若下一步要完成整条词的第四 range，最小的新证明目标是：在已经真实选择的复位桥及 R468 控制词上，使(29)的有限块函数、重复系数和原其它段，在**同一个**(44)的规范下同时为零，或者从其中某一完整函数导出实际不相容。这个目标必须使用最终路径的真实 $\omega$、完整第三 history 和平台响应；不能只增加相同保护芽的数目，也不能再使用间隙函数作不存在的自由度。

本稿没有宣称这个剩余联合问题已经可解，也没有证明它不可能。更未将全 period、多个保护芽、Klein 位置闭合或有限实际成本截面，提升为完整等距族、全局嵌入、reach 或宏观运动。它把可实际完成的二三阶同步归一与仍需实际支付的全段 ruling 分开，并给出两者之间全部真实传递项。

### 证明来源

- [R70：真实任意矩阵桥](R70-zero-matrix-bridges-and-affine-complete-fourth-period.md)；
- [R73：逐点八矩与局部第三](R73-pointwise-eight-matrix-and-local-third-bridge.md)；
- [R77](R77-weight-three-local-operator-actual-finite-controllability.md)、[R79](R79-closed-horizontal-C1-control-and-endpoint-potential.md)、[R80](R80-complete-third-affine-class-and-P1-endpoint-obstruction.md)：完整第三实际空间和共同窗口；
- [R83：完整二、三、四阶历史传递与真倒行](R83-true-fourth-transfer-and-zero-lower-history-variations.md)；
- [R184](R184-affine-linear-fixed-circle-fourth-range-with-second-gauge.md)、[R221](R221-complete-fixed-circle-ruling-moment-map-and-joint-right-inverse.md)：原完整 ruling 与三矩规范；
- [R406](R406-complete-weight-zero-natural-fluxes-and-canonical-joint-obstruction.md)：真实正成本；
- [R467](R467-conditional-actual-highest-gauge-control-and-one-complete-thirteen-row-normalization.md)、[R468](R468-real-height-pulse-fills-affine-residual-and-completes-actual-enhanced-cost-control.md)、[R469](R469-global-gauge-locking-and-real-prefix-obstructions-between-rational-germs.md)：同一增强、同一规范及相对前缀门。
