# R1036：原最低型的整交错测试与完整 MW 消去

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126。
global_route / o2_high_coefficient / root。

**已证明：在原 \(p\equiv11\bmod12\) 行，存在一个明确的整交错型，
由原特殊晶体、实际算术下降和真实本地 \(T_5\) 构造；
用完整原 \(\varepsilon^{-1}e_1\log P\) 作第一槽后，
所得实际 Lie 泛函消去原全部 Mordell–Weil 对数及其饱和格。**
不须在整格中任意选择一个简单商投影。
原 Jacobian 中相关因子的真实重数在下文单独支付。

该泛函可能为零或非本原。本篇给出其与同一个原 CM jet
的准确剩余域配对，**不宣称此配对已经是单位**。
整个 Serre 目标仍 OPEN。

## 1. 原整格与约定

设
\[
p=12g-1>37,\quad m=(p-1)/2,\quad
e_0=m(p+1),\quad \pi_0^{e_0}=p,\quad\varepsilon=\pi_0^m,
\]
保留原 \(J=J_1\)、\(P=(p-1)D_0\)、\(N=1+\delta+\delta^2\)。
R1029 的真实整幂等元 \(e_1\) 给 BT 因子 \(\mathcal G_1\)。
使用 R1035 的协变晶体及实际整同构
\[
M=M_H\oplus M_L,\qquad
M_L\otimes_W R\simeq\operatorname{Lie}\mathcal G_1.
\tag{1036.1}
\]
原 split-Hecke、实际本地 \(T_5\) 和 deck 作用通过此式搬运。
对 \(\delta_*\) 保留协变/Rosati逆约定；它不是自然曲线
\(\delta^*\) 的无说明替换。

在原特殊尾的基 \(f_s=[\psi_s]\)、\(\omega_s=dX_s/Y_s\) 上，
取杯积顺序
\[
\langle\omega_s,f_t\rangle=2\delta_{st},
\qquad
\langle f_s,\omega_t\rangle=-2\delta_{st}.
\tag{1036.2}
\]
这正对应已经固定的
\(\operatorname{Res}(f_s\omega_s)=-2\)，未改变 Serre 尺度。
极化在 \(M_H,M_L\) 内各为零，两格之间完美。

令 \(\alpha\) 是原模型的算术下降，作用于 \(W\) 为
\(p\)-次 Frobenius，并选 \(\alpha(\pi_0)=\pi_0\)
（full-\(p\) 图亦可取 \(\alpha(\varpi)=\varpi\)）。
关系 \(\alpha\sigma\alpha^{-1}=\sigma^p\)，以及 \(\alpha(\xi)=\xi^p\)，
说明 \(\alpha\) 分别保留两角色格 \(M_H,M_L\)；
而 \(F\) 与 \(\sigma\) 交换但半线性，所以 \(F\) 交换这两格。
晶体 Frobenius \(F\) 与 \(\alpha\) 相容且交换。
定义真正 \(W\)-线性的算子
\[
\Pi=F\alpha^{-1}.
\tag{1036.3}
\]
下面先证明它在本实际模型上满足 \(\Pi^2=-p\)，
不靠一个未经核准的全自守谱行列式假设。

## 2. 原 \(\mathbf F_{p^2}\) 尾及没有遗漏的下降相位

R1023 已证明所有原 \(e_1\) 超奇异点 \(s\in S\) 属于
\(\mathbf F_{p^2}\)，并给 source/target 的实际首项
\[
C_s^{p-1}=\frac1{g_sk_s^p}
   =U_{{\rm source},s}^{-1},
\qquad U_{{\rm target},s}=k_sg_s^p.
\tag{1036.4}
\]
两者不能互换。

每个原 **source** 也是同一个实际六标记超奇异族的对象。
在它的 \(\mathbf F_{p^2}\) 模型上，
\[
\operatorname{Fr}_{p^2}=[\pm p].
\tag{1036.5}
\]
这里的额外自同构必须检查：

- 对 \(j\ne0,1728\)，超奇异 \(V\) 与相对 Frobenius 都是
  纯不可分度 \(p\) 同源，故 \([p]=u\circ\operatorname{Fr}_{p^2}\)，
  \(u\in\operatorname{Aut}E=\{\pm1\}\)。
- 原 \(j=0\) 的 \(e_1\) 点是 \(s=0\)，模型
  \(y^2=x^3+1\) 定义于 \(\mathbf F_p\)。
  \(p\equiv2\bmod3\) 的立方双射给 Frobenius trace 为零，
  故平方为 \([-p]\)。
- 原 \(j=1728\) 点满足 \(s^3=1/2\)，模型为
  \(y^2=x^3+(3s/2)x\)。
  写 \(s=s_0\zeta^i\)、\(s_0\in\mathbf F_p\)。
  因 \(12\mid p+1\)，\(\zeta^i\) 是 \(\mathbf F_{p^2}\) 中四次幂，
  该曲线与 \(\mathbf F_p\) 上的 \(j=1728\) 模型同构。
  \(p\equiv3\bmod4\) 给后者 trace 零，故同样平方为 \([-p]\)。

这些结论分别用于 source；没有由 target 首项猜 source 首项。
取原 source 上定义于 \(\mathbf F_{p^2}\) 的形式参数，
其 \([p]\) 的 \(T^{p^2}\) 首系数于是为 \(\pm1\)。
特殊形式群的全部端同态在 \(\mathbf F_{p^2}\) 定义：
算术平方以 (1036.5) 的标量共轭它们，因此作用平凡。
故 R1021 的真实 \(\mu_{p^2-1}\) framing 与单位平均
可在 \(\mathbf F_{p^2}\) 上进行，仍保持这个实际来源。
由 (1036.4) 得
\[
C_s^{p-1}=\pm1,\qquad C_s\in\mathbf F_{p^2},\qquad
A_s=-3C_s^2\in\mathbf F_p^\times.
\tag{1036.6}
\]

原普通尾的同一个正规化子商为
\[
D_s:\quad Y^2=X\left(X^{(p+1)/2}+A_s\right).
\tag{1036.7}
\]
还须核它的 \(\mathbf F_{p^2}\) 模型就是实际算术平方的模型。
若 (1036.5) 为 \(-p\)，则 \(-p\equiv1\bmod6\)，六标记无修正。
若为 \(+p\)，则 \(p\equiv-1\bmod6\)，修正恰为共同 \([-1]\)；
其在两个 full-\(p\) level 参数上的共同反号已由
\(N_{\rm ns}\) 中的 \(-I\) 杀去。
\(j=0,1728\) 已单独排除额外的 \(\mu_3,\mu_4\) 相位。
所以 \(\alpha^2\) 在 (1036.7) 上没有未记入的 deck 或四次扭曲。

## 3. Hermitian 切线证明实际 Frobenius 平方

令 \(n=(p+1)/2\)。
对任意 \(A\in\mathbf F_p^\times\)，可在 \(\mathbf F_{p^2}\) 取
\(a^n=A\)。此时
\(\operatorname{Norm}(a)=A^2\)，故 \(a\) 是
\(\mathbf F_{p^2}\) 中平方；\(aA\) 也为平方。
取 \(b^2=aA\)，则
\[
X=aX_1,\qquad Y=bY_1
\]
给 \(D_1\simeq D_A\) 的真实 \(\mathbf F_{p^2}\) 同构。

Hermitian 曲线
\[
\mathcal H:\quad V^{p+1}=U^{p+1}+W^{p+1}
\]
在仿射图有到 \(D_1\) 的非恒定态射
\[
X=u^2,\qquad Y=u\,v^{(p+1)/2}.
\tag{1036.8}
\]
以下直接证明 \(\operatorname{Fr}_{p^2}=[-p]\) 于
\(\operatorname{Jac}\mathcal H\)，不用数值点数。

对任意几何点 \(Q\)，其切线 \(L_Q\) 与 \(\mathcal H\) 的交因子为
\[
p[Q]+[\operatorname{Fr}_{p^2}Q].
\tag{1036.9}
\]
确实，把 \(Q+tQ'\) 代入方程，常数和一次项因曲线方程及
切线条件消失，剩余从 \(t^p\) 开始；另一方面
\(\operatorname{Fr}_{p^2}Q\) 在该切线上，因为代入切线的值
是原曲线方程在 \(Q\) 的 \(p\) 次幂。
当 \(\operatorname{Fr}_{p^2}Q=Q\) 时，可取 \(Q\) 的
\(\mathbf F_{p^2}\) 坐标；\(t^p\) 项的系数正是已消失的一次项
系数的 \(p\) 次幂，因而也为零，交阶为 \(p+1\)。
结合总交数 \(p+1\)，这证明 (1036.9) 的全部情形。

取 \(\mathbf F_{p^2}\) 点 \(Q_0=[1:1:0]\)（坐标顺序 \(U,V,W\)）。
其切线交因子为 \((p+1)[Q_0]\)。
所以函数 \(L_Q/L_{Q_0}\) 主化
\[
p(Q-Q_0)+(\operatorname{Fr}_{p^2}Q-Q_0).
\]
这些点差生成 Jacobian，故 Frobenius 等于 \([-p]\)。
(1036.8) 的 Jacobian norm 满射且与 Frobenius 交换，
所以相同结论传到 \(D_1\)，再经上述同构传到每个实际 \(D_s\)。

R1029 的最低 \(\pm m\) 晶体只来自这些 \(e_1\) 尾的最低一对；
中心和 \(e_3\) 尾没有这两个角色。
结合 §2 对实际算术下降的核对，遂有
\[
F^2=-p\,\alpha^2\quad\text{于 }M,\qquad
\boxed{\Pi^2=-p.}
\tag{1036.10}
\]
这是本实际模型的等式，不由任意超奇异模型替换而来。

## 4. 真整对称型与交错型

极化相容性给
\[
\langle Fx,Fy\rangle
   =p\,\operatorname{Frob}\langle x,y\rangle,\qquad
\langle\alpha x,\alpha y\rangle
   =\operatorname{Frob}\langle x,y\rangle.
\]
故 \(\Pi^\dagger\Pi=p\)。由 (1036.10) 得
\[
\Pi^\dagger=-\Pi.
\tag{1036.11}
\]
R1035 已证明 \(F:M_L\to M_H\) 为整单位同构；
\(\alpha\) 保 \(M_L\)，因此
\[
B(v,w)=\langle\Pi v,w\rangle,\qquad v,w\in M_L,
\tag{1036.12}
\]
是整、对称、完美的 \(W\)-双线性形式。

为简记，以下用 \(\delta\) 表示真正 \(\delta_*\) 的协变晶体作用。
有 \(\delta^\dagger=\delta^{-1}\)，
\(\alpha\delta\alpha^{-1}=\delta^{-1}\)，而 \(F\) 与 \(\delta\) 交换。
所以
\[
\Pi\delta=\delta^{-1}\Pi,\qquad
B(\delta v,w)=B(v,\delta w).
\]
取外部 \(W\)-线性算子
\[
D=\frac{\delta-\delta^{-1}}{\zeta-\zeta^2}.
\tag{1036.13}
\]
它是 \(B\)-自伴；此处不把含外部系数的 \(D\) 称为 BT 端同态。

原 \(T_5\) 在 \(\mathbf Q_p\) 上真实定义、Rosati 自伴，
并与 \(F,\alpha\) 相容，因此也为 \(B\)-自伴。
原完整对应关系给 \(T_5\delta=\delta^{-1}T_5\)，从而
\(T_5D=-DT_5\)。
故
\[
\boxed{\quad
\mathscr A(v,w)=B(v,T_5D w)
\quad}
\tag{1036.14}
\]
是整交错型。
它通过 (1036.1) 成为实际 Lie 格上的整交错型。
全部原 split \(T_\ell\) 与 \(\Pi,T_5,D\) 交换且为 Rosati 自伴，
于是
\[
\mathscr A(T_\ell v,w)=\mathscr A(v,T_\ell w).
\tag{1036.15}
\]
下一节把这个平衡性扩到真正所需的 \(F_0\)，并处理同源重数。

## 5. split-Hecke 确实生成所需中心 \(F_0\)

本节只对原 \(D_0\) 投影**非挠**的非 CM paired block 使用
R1011 的条件证明。该文较大的 \(p\) 下界用来保证这种块存在；
其 §§2–5 在非挠假设给定后没有再使用那个下界。

沿用其实际数据
\[
K=\mathbf Q(\zeta_3),\quad L=K(\sqrt[3]4),\quad
W_\tau=\operatorname{Ind}_{G_K}^{G_{\mathbf Q}}
              (V_\tau|_{G_K}\otimes\kappa),
\]
以及
\[
B_{\rm aux}\sim_{\mathbf Q}C^h,\quad
\operatorname{End}_{\mathbf Q}^0(B_{\rm aux})=M_h(F_0),\quad
F_0\subset F,\quad [F:\mathbf Q]=h[F_0:\mathbf Q].
\tag{1036.16}
\]
这里用 \(h\) 表示辅助限制标量的同源重数，以免与局部深度 \(m\) 混淆。
R1011 已排除非平凡 Schur 指数，且
\[
\dim C=2[F_0:\mathbf Q],\qquad
C(\mathbf Q)\otimes\mathbf Q=F_0\beta
\tag{1036.17}
\]
对任一该块中非挠的原点像 \(\beta\) 成立。

置
\[
F_s=\mathbf Q(a_\ell:\ell\nmid6p,\ \ell\equiv1\bmod3)\subset F.
\]
对两个系数嵌入 \(\tau,\tau'\)，有
\[
W_\tau\simeq W_{\tau'}
\quad\Longleftrightarrow\quad
V_\tau|_{G_K}\simeq V_{\tau'}|_{G_K}.
\tag{1036.18}
\]
反向直接诱导。正向则限制到 \(G_K\)：
\(\kappa\) 与 \(\kappa^{-1}\) 两个不可约组成部分不能交叉配对，
因为它们的行列式
\(\chi_{\rm cyc}\kappa^2,\chi_{\rm cyc}\kappa^{-2}\) 不同。
这里保留真实三次角色，未用普通二次诱导替换。

由 \(G_K\) 上的 Chebotarev 和 Brauer–Nesbitt，
(1036.18) 的右侧恰等价于所有 split \(a_\ell\)
在两个嵌入下相同。
另一方面 (1036.16) 中 \(F\) 是 \(M_h(F_0)\) 的极大子域；
按 \(F\) 嵌入分解 Tate 模，同一 \(F_0\) 嵌入上有
\(h\) 个同构的 \(W_\tau\)，不同中心嵌入的组成部分不同构。
故 \(F_s,F_0\) 在 \(F\) 的所有嵌入上定义相同等价类。
首先 split \(a_\ell\) 在每个同构类上相同，故属于中心 \(F_0\)；
再由相同等价类排除严格子域，得到
\[
\boxed{F_s=F_0.}
\tag{1036.19}
\]
所以 (1036.15) 真的给出全部 \(F_0\otimes\mathbf Q_p\) 平衡性，
而不止某个整 Hecke order 的平衡性。

两个不可约二维 \(G_{\mathbf Q}\) 表示若在 \(G_K\) 限制同构，
延拓只可能相差 \(1\) 或 \(\chi_{-3}\)。
非 CM 排除自扭曲等于自身，故
\[
h=[F:F_s]\le2.
\tag{1036.20}
\]
这个结论尚未说原 \(J_1\) 的重数为一；下一节单独核它。

## 6. 原 Jacobian 的相关因子只出现一次

先消费 R970 §5 已证明的实际 \(H_6\) 图式 multiplicity，
包括 (970.22)–(970.24a) 的两配对分量重建，不重新多乘二。
本处补入的实际局部数据是 R1010 §3 与 R1029：

| 位置 | 原新部分的完整允许输入 | 所需固定方向重数 |
|---|---|---|
| \(2\) | 未分歧主系列 \(1\oplus{\rm Std}_2\)，或未分歧 Steinberg 的 \({\rm Std}_2\) | \({\rm Std}_2\) 各一次 |
| \(3\) | 唯一中央平凡 depth-zero cusp \({\rm Std}_3={\rm Std}_2\circ\vartheta\) | 一次 |
| \(6\) 的图条件 | \(({\rm Std}_2\otimes{\rm Std}_3)^{H_6}\) | 一维 |
| \(p\) | 原允许类型的 \(N_{\rm ns}\)-固定线；特别是 \(\tau_1\) | 一维 |
| 其他有限处 | 球面向量 | 一维 |

有限 \(\operatorname{PGL}_2(\mathbf F_p)\) 的各不可约表示，
其非分裂 torus character 平均为零或一；
正规化子固定空间包含在该 torus 固定空间中，故至多一维。
实际出现的 \(\tau_1\) 由 R1029 的奇偶计算给恰一维。

二处的一维超尖点固定型在 \(A_3\) 上平凡，已由原 \(N=0\)
排除；三处的主系列/特殊型不含所需 \({\rm Std}_3\)。
在 \(p\) 处没有额外旧球面复制，因去掉 \(p\) 水平后
\(S_2(H_6)=0\)；完整正规化子奇偶条件由 R1029 保留。
因此每个 canonical 自守表示在相关原新部分出现一次。

原关系
\[
\jmath=\delta-\delta^2,\qquad
\jmath^2=-3,\qquad
T_\ell\jmath=\chi_{-3}(\ell)\jmath T_\ell
\]
使非 CM 成分准确配成 \(\pi,\pi\otimes\chi_{-3}\)；
两者都在原谱内。
记 \(d=[F:\mathbf Q]\)。于是：

- 若它们属于不同有理 Galois 轨道，则 \(h=1\)。
  canonical paired block 的维数为 \(2d\)，而 R1011 的
  \(C\) 也为 \(2d\) 维。
- 若它们属于同一有理轨道，则 \(h=2\)。
  canonical block 只有 \(d\) 维；辅助簇虽为 \(C^2\)，
  此时 \(\dim C=d\)。

三次 \(\kappa_4\) 扭曲保持这些维数。
R1011 的真实 \(\Psi\) 在此原块上非零，因为原点像非挠；
其像在 \(B_{\rm aux}\sim C^h\) 中。
每种情形下源维数都恰为 \(\dim C\)，所以其像只能是一份 \(C\)，
且核有限。故
\[
\boxed{\quad
\text{原 \(J_1\) 的每个相关非 CM、\(D_0\) 非挠 paired block
同源于一次 \(C\)。}
\quad}
\tag{1036.21}
\]
没有将辅助限制标量的 \(h=2\) 偷换成 \(h=1\)。
对原点投影挠性的其他块，本篇不作半秩或重数断言。

不同非 CM paired blocks 由 split-Hecke 分离：
限制到 \(G_K\) 同构只产生上述同一个二次扭曲配对。
它们也不会与 CM 块混淆。
所以在特征零，(1036.15) 使不同块对 \(\mathscr A\) 正交。
这是有理分解的结论，不要求这些投影在原整数环中整。

## 7. 用完整原 log 得到全部 MW 消去

通过 (1036.1) 写
\[
v=\varepsilon^{-1}e_1\log P\in M_L\otimes R.
\tag{1036.22}
\]
它的整性来自 R1023 的**完整**首 log 与全部分母控制、
R1029 的整投影；这里没有把首层向量当成整个 log。

对实际 \(\operatorname{Lie}J\) 定义
\[
\boxed{\quad
\Lambda(w)=\mathscr A(v,e_1w).
\quad}
\tag{1036.23}
\]
这是原整 Lie 格上的 \(R\)-值线性泛函。
在特征零的 paired block 分解中：

1. 若原 \(D_0\) 投影为挠点，则第一槽的完整 log 为零。
   不需要对该块的秩作任何断言。
2. 若投影在非 CM 块中非挠，由 (1036.21) 原块是一份 \(C\)，
   且 (1036.17) 给完整 MW 空间为 \(F_0\beta\)。
   对任意 \(a\in F_0\otimes\operatorname{Frac}(R)\)，
   交错性与平衡性给
   \[
   \mathscr A(v,av)=\mathscr A(av,v)
                  =-\mathscr A(v,av)=0 .
   \]
   因 \(p\ne2\)，这确实为零。
3. 原旧部分由 \(D\) 杀掉；在 \(p\equiv11\bmod12\) 行，
   R1010 §3 的完整 CM 域审计表明全部 CM 新部均为
   \(\mathbf Q(\sqrt{-3})\)-CM，故原 \(T_5\) 为零。
   \(\delta\) 保持 CM 部分，故 \(T_5D\) 亦杀它。
   各非 CM paired blocks 与 CM 块的交叉项由 split-Hecke 正交消失。

于是
\[
\boxed{\quad
\Lambda\bigl(\log J(\mathbf Q)\bigr)=0.
\quad}
\tag{1036.24}
\]
整性和线性再给其 \(\mathbf Q_p\)-span、闭包，
以及与原整 Lie 格相交的饱和格上的消失。
这一步不选取整简单商投影，也没有清除一个未知的同源分母。

这里证明的是**由原点 \(P\) 定义的这个泛函**消去全部 MW。
没有声称辅助 \(B_{\rm aux}=C^2\) 的整个 MW 空间
由任意 \(F_0\)-平衡交错型都自动消去。
(1036.21) 正是避开该错误所需的实际重数结论。
也没有由 (1036.24) 宣称 \(\Lambda\) 非零或本原。

## 8. 同一个原特殊基中的明确配对

R1021/R1023 的真实 Dickson Čech 恒等式为
\[
\psi_s^p=\mathcal D_s-C_s^{p-1}/\psi_s .
\]
\(\mathcal D_s\) 是实际仿射尾的全局正则函数；
\(\psi_s\) 只按原节点的局部来源使用。
在 de Rham Čech 复形中用两边的这两个消去函数，
\(\bar F(f_s)\) 由 \(d\mathcal D_s\) 表示。
原节点有 \(\psi_s=z_s^{-m}+\)更高项，故
\[
d\mathcal D_s=mC_s^{p-1}z_s^{m-1}dz_s+\cdots .
\]
最低惯性角色的 Hodge 线由 \(\omega_s\) 唯一生成，
而其首项为 \(-2z_s^{m-1}dz_s\)。
因此
\[
\boxed{\quad
\bar F(f_s)=-\frac m2 C_s^{p-1}\omega_s
           =\frac{C_s^{p-1}}4\omega_s .
\quad}
\tag{1036.25}
\]
后一等式在剩余域中，因为 \(m\equiv-1/2\bmod p\)。
这只计算所需特殊映射，不擅自指定完整整 Frobenius 矩阵的所有项。

置原归一的
\[
e_s=\theta_s f_s,\qquad
q_s=C_s^{p-1}\theta_s^{p+1}
   =-\frac{(1-s^3)^{8g-2}}{A_p'(s)^2}.
\tag{1036.26}
\]
原节点式 \(b-s=\varepsilon\theta_s\psi_s\) 的主部与
\(\alpha(\varepsilon)=\varepsilon\) 给准确运输
\(\alpha(e_s)=e_{s^p}\)。
由 (1036.25)、\(\Pi=F\alpha^{-1}\) 和 (1036.2)，
先得到
\[
\bar B(e_s,e_t)=\frac{q_{s^p}}2\,{\bf1}_{t=s^p}.
\]
\(B\) 的对称性遂给 \(q_s=q_{s^p}\)；
(1036.26) 的有理 \(\mathbf F_p\) 来源又给
\(q_{s^p}=q_s^p\)。所以
\[
\boxed{\quad
q_s\in\mathbf F_p^\times,\qquad
\bar B(e_s,e_t)=\frac{q_s}2\,{\bf1}_{t=s^p}.
\quad}
\tag{1036.27}
\]
这里已包含 \(\alpha^{-1}\) 的指标置换。
\(B\) 是双线性的；不可再对任意外部共乘单位另取 \(p\) 次幂。

R1023 的完整原首 log 和 R1032 的原 jet 分别给
\[
\bar v=\sum_{s\in S} a_s e_s,\qquad
a_s=\lambda(s)+R_p(s),
\]
\[
J=\sum_{s\in S}\frac{e_s}{(1-s)^2}.
\tag{1036.28}
\]
在这个**同一个**格上，记原真实 \(T_5D J\) 的坐标为
\[
T_5D J=\sum_{s\in S}H_s e_s .
\]
全部矩阵作用在这里都是原对应，不任换一个有同型的矩阵。
定义准确有限值
\[
\boxed{\quad
K_p=\bar B(\bar v,T_5D J)
     =\frac12\sum_{s\in S}q_s a_s H_{s^p}.
\quad}
\tag{1036.29}
\]
原有理函数 \(\lambda+R_p\) 满足 \(a_{s^p}=a_s^p\)，故亦可写成
\(\frac12\sum q_s a_s^p H_s\)。
是否 \(K_p\ne0\) 是下一项真实待证问题。

令 \(w=(a-1)/p^3\)、\(n_0=4g-1\)，并保留 R1033
同一个单位 \(\lambda_0=(d\bar z/dt)(Q)\)。
对原 Abel 映射，(1036.23) 给实际 MW 消去函数
\[
\mathcal F(w)=
 \Lambda\left(\frac1{p\varepsilon}\log[x(w)-c_1]\right).
\tag{1036.30}
\]
这里 \(x(w)\in X_1\) 表示原圆盘上的曲线点；
所有有理点代入 (1036.30) 都为零。
R1033 的完整尾界经整泛函保持；约化后的次数至多 \(n_0\)。
最高项准确为
\[
\boxed{\quad
[w^{n_0}]\overline{\mathcal F}
 =-\frac{\kappa_1\sqrt{A_{\rm tail}}}{m}\,
           \lambda_0^{-n_0}\,K_p.
\quad}
\tag{1036.31}
\]
该式保留原 \(\theta_s,\kappa_1,\sqrt{A_{\rm tail}},\lambda_0\)
及 Serre 负号；没有归一掉未知单位。

## 9. 继续要完成的原问题

下一步须计算实际 \(T_5D\) 的全部六条路径及 (1036.29)，
证明原 \(K_p\) 非零或换一个真正有效的实际消去泛函。
即使最高项成为单位，R1033 已指出原低 \(w\) 系数和深盘零点
仍须控制；不能仅据最高次数界宣称只有中心一个零点。
本篇不为指定 Néron 商格作无来源的饱和断言。

整个 \(p\equiv5\bmod12\) 行亦有不同的 Raynaud/两中心几何，
不把本篇的 compact-type 好模型直接搬过去。
R1003/O0 的完整惯性、非整 \(j\)、变化 CM 域等全局支路继续开放。

## 来源与审核

- [R1029](R1029-original-lowest-inertia-type-integral-Hecke-splitting.md)、
  [R1035](R1035-original-lowest-type-integral-Lie-comparison-by-two-PD-thickenings.md)：
  真实整类型块与实际 Lie 格比较。
- [R1021](R1021-actual-full-p-affine-tail-rigidity-and-quotient-parameter.md)、
  [R1023](R1023-original-CM-divisor-complete-first-log-vector.md)：
  原 framing/Dickson、source/target 首项、节点运输及完整首 log。
- [R1032](R1032-original-lowest-type-complete-CM-normal-jet-functional.md)、
  [R1033](R1033-original-rational-CM-disc-exact-lowest-type-scale-and-tail.md)：
  原 CM jet、Serre 尺度、有理参数和全部尾界。
- [R1010](R1010-original-CM-divisor-nontorsion-in-nonCM-part.md)、
  [R1011](R1011-original-nonCM-half-rank-quotient-and-rational-CM-jet-transversality.md)：
  实际全部六水平型、完整 CM 域、真实 \(\Psi\)、Nekovář 条件证明、
  \(B_{\rm aux}\) 的 Schur 指数/秩与同源重数。
- [R970 §5](R970-original-Cartier-packet-and-high-CM-congruence-ideal.md)：
  已登记的完整图式 multiplicity 和两配对分量重建。
  本篇另保二处 Steinberg、原 \(p\) 型及三次扭曲后的实际维数，
  不重做旧低层结论。

global_route、o2_high_coefficient 与 root 纸核 source 与 target 的区别、
特殊 \(j\) 的全部相位、真正 \(\mathbf F_{p^2}\) framing、
Hermitian 切线主因子、协变 Frobenius/极化、全部中心和实际重数，
并核完整 log 的 MW 消去与原 jet 的所有单位。
没有数学程序执行、没有旧窗口重算，未把 \(K_p\) 当作已经非零。


## R1037 后继：实际本原整泛函

[R1037](R1037-original-Hodge-graph-operator-and-primitive-MW-annihilator.md)
由实际 Hodge graph 构造另一算子 \(\mathcal Q\)，
证明其原负 deck 模 \(\pi_0\) 作用单射，
从而给出消去全部 MW 饱和格的本原整泛函
\(B(v,\mathcal QD\,\cdot)\)。
这不声称本篇 \(T_5\) 版本自动本原；
两个指定 CM 读数及原盘最低单位项仍须各自核对。
