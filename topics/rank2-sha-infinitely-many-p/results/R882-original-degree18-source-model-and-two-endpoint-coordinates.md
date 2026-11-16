# R882 — 原十八倍源的显式椭圆模型与两个 endpoint 坐标

日期：2026-11-16。

**状态：原 degree18 源覆盖、\(q_0/q_2\) 的显式 level9 坐标、完整17-Hecke方块及两份原坐标证书的函数域消费公式已证明。源椭圆曲线与 Frobenius-shadow 的目标 \(E_0\) 是不同拷贝。尚未运行完整有限域求交，也未声称原 \(Z_{\rm orig}\) 的 shadow 非零。**

本篇使用 R848 的同一 \(q_6:X_0(10404)\to X_0(867)\)，并保
R831 的 \(q_0(z)=z,\ q_2(z)=4z\)。不把原循环换成 level36 上的循环；
level36 曲线只是原大源在 degree18 底覆盖中的明确坐标模型。

## 1. 两个固定 Hauptmodul 及准确的三次关系

置
$$
T_9(q)=\left(\frac{\eta(q)}{\eta(q^9)}\right)^3,\qquad
A(q)=T_9(q)+3
=q^{-1}+5q^2-7q^5+3q^8+\cdots,
$$
$$
T_3(Q)=\left(\frac{\eta(Q)}{\eta(Q^3)}\right)^{12}
=Q^{-1}-12+54Q+\cdots .
\tag{1}
$$
均采用所显示的 eta 商和首项，不允许另作平移或缩放。
在 \(X_0(9)\) 上准确有
$$
\boxed{T_3(q^3)=A(q)^3-27.}
\tag{2}
$$
例如两边都是只在 \(\infty\) 有三阶极点的模函数；
显示展开取消全部负次项后，差是常数，而常数正是 \(-27\)。
这也固定 R866 所用中央三阶相位。

在中央参数 \(Q_9\) 上，prime-to-9 的 \(T_2\) 三个邻点是
$$
A(Q_9^2),\quad A(Q_9^{1/2}),\quad A(-Q_9^{1/2}).
$$
其三个基本对称式分别为
\(A(Q_9)^2,\ 9A(Q_9),\ 54-A(Q_9)^3\)。因此
$$
\boxed{\Psi_2(A,B)=A^3+B^3-A^2B^2+9AB-54=0.}
\tag{3}
$$
这里可以完全由 (1) 的有限主部证明：三个对称式在 \(X_0(9)\)
上除 \(\infty\) 外无极点，故是 \(A\) 的多项式；
其极阶和常数依次给 \(A^2,9A,54-A^3\)。
例如末式的主部和常数为 \(-Q_9^{-3}+39\)，与
\(54-A(Q_9)^3\) 一致。这不是只检查几个系数后猜一个模多项式。

## 2. 原 \(X_0(36)\) 的源坐标

令
$$
E_{\rm src}:\quad y_s^2=x_s^3+1,\qquad v_s=x_s^3.
\tag{4}
$$
这是源曲线的一份独立拷贝；后文的目标 Frobenius
\(E_0:Y^2=X^3+1\) 仍用 R859 的坐标和作用。

在 (4) 上定义
$$
A=\frac{v_s+4}{x_s^2},\qquad
B_2=\frac{v_s-2}{x_s},
$$
$$
B_0=\frac{5v_s+8-y_s(v_s-8)}{x_s^4},\qquad
B_1=\frac{5v_s+8+y_s(v_s-8)}{x_s^4}.
\tag{5}
$$
直接代入 \(y_s^2=v_s+1\) 得
$$
B_0+B_1+B_2=A^2,\quad
B_0B_1+B_1B_2+B_2B_0=9A,\quad
B_0B_1B_2=54-A^3.
\tag{6}
$$
所以三者正是 (3) 的全部根。

反向，在非空开集上
$$
\boxed{
x_s=\frac{6B_2-2A^2}{A^2B_2-B_2^2-6A},\qquad
y_s=\frac{x_s^4(B_1-B_0)}{2(x_s^3-8)}.
}
\tag{7}
$$
例如第一式的分子、分母在 (5) 下分别为
\(4(v_s-8)(v_s+1)/x_s^4\) 和
\(4(v_s-8)(v_s+1)/x_s^5\)，故准确还原 \(x_s\)。
这些是函数域等式；分母为零的点由射影正规化保留。

\(A:E_{\rm src}\to\mathbf P^1\) 的次数为6：
\(x_s\) 满足 \(x_s^3-Ax_s^2+4=0\)，再加 \(y_s^2=x_s^3+1\)。
由 (7)，(4) 的函数域恰为 (3) 的完整 splitting field。
另一方面，R848 在 \(M=9\) 的同一群计算给
$$
\operatorname{diag}(2,1)\Gamma_0(36)\operatorname{diag}(2,1)^{-1}
=\Gamma_0(9)\cap\Gamma(2),
$$
其 mod2 商为 \(S_3\)。因此这个 splitting field 正是原
\(q_1:X_0(36)\to X_0(9)\) 的函数域，而非另一个同 \(j\) 的曲线。

选择原 Tate cusp 后，由 (7) 和 (1) 得
$$
x_s=q^{-2}+O(q^4),\qquad y_s=-q^{-3}+O(q^3),
$$
$$
\boxed{
A=A(q^2),\qquad B_0=A(q),\qquad B_2=A(q^4),\qquad B_1=A(-q).
}
\tag{8}
$$
因而 (5) 已逐一固定 \(q_0,q_2\)，不是未标号的三个根。
如需源微分，其首项和 \(S_2(36)\) 的一维性给
\(dx_s/(2y_s)=\eta(q^6)^4\,dq/q\)；
这只是源坐标的规范，不替代 R878 中新第一因子 \(F\) 的微分。

## 3. 完整 degree18 底覆盖

由 (2)、(5)，置
$$
\boxed{
T=A^3-27
=\frac{(v_s+1)(v_s-8)^2}{v_s^2}.
}
\tag{9}
$$
\(T\) 在 \(E_{\rm src}\) 上的次数为18，并在原 cusp 等于
\(T_3(q^6)\)。原中央 \(R:z\mapsto z+1/3\) 是
$$
R(x_s,y_s)=(\omega x_s,y_s).
\tag{10}
$$
原 \(S:z\mapsto z+1/2\) 则是 \((x_s,y_s)\mapsto(x_s,-y_s)\)。
\(S_3\) 置换 \(B_0,B_1,B_2\)，固定 \(A\)；中央 (10)
与它交换。因此几何 deck 群恰为 \(C_3\times S_3\)。

群层面也直接付清原源。写 \(w=6z\)，则
$$
\operatorname{diag}(6,1)\Gamma_0(36)\operatorname{diag}(6,1)^{-1}
=\{\pm I\}\Gamma(6),
$$
在 \(\Gamma_0(3)\) 内指数18。加入原 \(17^2\) 条件后，
$$
\operatorname{diag}(6,1)\Gamma_0(10404)\operatorname{diag}(6,1)^{-1}
=\Gamma_0(867)\cap\{\pm I\}\Gamma(6).
\tag{11}
$$
CRT 给 mod6 商仍满，所以这个交的指数仍18。
于是
$$
\boxed{
X_0(10404)
=\operatorname{Norm}\!\left(
 X_0(867)\times_{X_0(3)}E_{\rm src}\right)
}
\tag{12}
$$
是有标号的原函数域/光滑射影曲线等式。
底上 \(T=T_3(Q)\)，\(Q=q^6\)。右边必须取正规化，
不能把奇异纤维积的仿射零点直接当闭点。

覆盖 (9) 的全部几何分支可显式列出：

| 底值 | 源点 | 分歧指数 |
|---|---|---:|
| \(T=0\) | \(y_s=0\)，或 \(x_s^3=8\) | 2 |
| \(T=-27\) | \(x_s^3=-4\) | 3 |
| \(T=\infty\) | \(O,(0,1),(0,-1)\) | 6 |

分别为9、6、3个几何点。没有额外分支。
在 \(r=29\) 或41处均为 tame 覆盖；但 base change 仍可能取消或分裂
这些分歧，所以 (12) 的正规化和每个地方的实际重数始终保留。

## 4. \(X_0(867)\) 的真实17塔与中央 level9 坐标

令 \(\Phi^{(3)}_{17}(T,U)\) 是按 (1) 的 \(T_3\) 规范生成的单次17-Hecke
多项式。它可用同 R869 的 Faber/Newton 方法精确生成：
eta 对数系数改为
\(-12\sigma_1(n)+36[3\mid n]\sigma_1(n/3)\)，Faber 阶数至306；
不借用不同 Hauptmodul 的同名多项式。

原底函数域采用非回溯塔
$$
\Phi^{(3)}_{17}(T,U)=0,\qquad
\frac{\Phi^{(3)}_{17}(U,V)}{V-T}=0,
\tag{13}
$$
其中原 cusp 为
$$
T=T_3(Q),\quad U=T_3(Q^{17}),\quad V=T_3(Q^{289}).
$$
次数分别18、17，底到 \(X_0(3)\) 总次数306。
去掉 \(V=T\) 是去掉真实 dual 回溯支，不是删除一个误差项。

用 R869 已固定的原 level9 多项式
$$
\Psi^{(9)}_{17}(A,B)
=\Phi^{(9)}_{17}(A-3,B-3).
$$
在 (12) 的函数域内，中央两个后继 \(A_1,A_2\) 唯一由
$$
\gcd\bigl(Z^3-U-27,\ \Psi^{(9)}_{17}(A,Z)\bigr),\qquad
\gcd\bigl(Z^3-V-27,\ \Psi^{(9)}_{17}(A_1,Z)\bigr)
\tag{14}
$$
的 monic 一次因子读取。它们的原展开是
\(A(q^{34})\)、\(A(q^{578})\)。

(14) 的一次性是模问题中的真实兼容：
prime-to-3 的17同源在给定 cyclic3数据上有唯一相容的返回。
也可在一般非 CM 椭圆曲线上用 \(\operatorname{End}=\mathbf Z\)
核其唯一性。计算在整个函数域做 gcd；
不能在一个特殊 CM 点上 gcd 跳阶后重新挑根。

## 5. 两个原 endpoint 的完整三个坐标

令 \(i=0,2\)，先用 (5) 固定 \(B_{i,0}=B_i\)。
按序取
$$
\boxed{
B_{i,k}=
\text{根}\left[
\gcd\bigl(\Psi_2(A_k,Z),
          \Psi^{(9)}_{17}(B_{i,k-1},Z)\bigr)
\right],\quad k=1,2,
}
\tag{15}
$$
其中 \(A_0=A\)。
这些 gcd 在原函数域中同样为 monic 一次：
2与17互素，给定一条17同源和一个2核，后者的像给唯一的2–17
交换方块。一般点上不会有第二条相同的非回溯方块。
原几何 source 决定此方块，不需要额外 source 或有限角色。

于是整个 \(q_0/q_2\) 在 level9 三坐标中准确为
$$
q_i:\quad
(T_9,T_9[17],T_9[289])
=(B_{i,0}-3,B_{i,1}-3,B_{i,2}-3).
\tag{16}
$$
供底上 RR 函数求值的三坐标则是
$$
\boxed{(T_i,U_i,V_i)
=(B_{i,0}^3-27,\ B_{i,1}^3-27,\ B_{i,2}^3-27).}
\tag{17}
$$
这把同一个 \(X_0(867)\) 函数的两个 pullback 完全具体化。
有限域实现先生成 (14)/(15) 的全局有理函数，再在正规化后的地方求值，
不在每个闭点作无标号的邻点搜索。

## 6. RR 基与所有 cusp 的准确连接

在底 \(B=X_0(867)\) 上取
$$
S(Q)=E_3(Q)=\frac{3E_2(Q^3)-E_2(Q)}2
=-D_Q\log T_3(Q),\qquad S(0)=1.
$$
定义真实除子
$$
D_S=\operatorname{div}(dT/T)+\sum_{\rm all\ cusps}[c].
\tag{18}
$$
它有效，次数204，且在 \(\infty\) 的系数为0。
故
$$
M_{2m}(867)/S^m=L(mD_S).
\tag{19}
$$
特别 \(L(D_S)\) 维数120；其前205项在原 \(Q\) cusp 精确确定函数。
(19) 保留全部 cusp，不能只在 \(T\ne0,\infty\) 的仿射开集解核。

R881 允许在两份特征零坐标已经认证后，直接用固定好素数的高精度
整 germ 恢复这两个 RR 比值，不必重播特征零 CRT。
本篇只给它们消费所需的原函数域嵌入；
不以特征 \(r\) 的微分方程唯一性取代 R881 的前提。

## 7. 第一因子 \(F\) 在这条源上的直接读取

若 R878 的完整特征零证书成功，则使用其中的
\(V=\eta(Q)^{12}y_F\)，令
$$
v_F=V/S^3\in K(B).
$$
在 \(X_0(3)\) 上的准确恒等式为
$$
\frac{E_4}{S^2}=\frac{T+243}{T+27},\quad
\frac{E_6}{S^3}=\frac{T^2-486T-19683}{(T+27)^2},\quad
D:=\frac{\Delta}{S^6}=\frac{T^3}{(T+27)^4}.
\tag{20}
$$
例如由 \(S\) 在唯一阶3椭圆点的零阶和 valence，左边的极点全部位于
\(T=-27\)；两个 cusp 的阶及首项逐一给 (20)。
也可清分母后以这些低权的 Sturm 界核验，但本篇不增加数值执行。

令
$$
y_s'=\frac{y_s(x_s^3-8)}{x_s^3},\qquad
\boxed{\varepsilon=-\,\frac{T\,y_s'}{A^6}.}
\tag{21}
$$
由 \((y_s')^2=T\)、\(A^3=T+27\) 得 \(\varepsilon^2=D\)。
在原 cusp，\(y_s'\sim-q^{-3}\)，故
\(\varepsilon\sim q^3\)，准确是
\(\eta(Q)^{12}/S^3\)，不是其负号。

已认证坐标还保证下面的底函数是完美三次幂：
$$
R_F^3=\frac{v_F^2-17D}{D(T+27)},\qquad R_F(\infty)=1.
\tag{22}
$$
在固定系数域中，值1唯一指定三个根中的原根。这里的完美三次幂及其原根以已成功的特征零坐标证书和良好约化为前提。于是
$$
\boxed{x_F=A R_F,\qquad y_F=v_F/\varepsilon.}
\tag{23}
$$
它满足 \(y_F^2=x_F^3+17\) 及原主项
\(x_F\sim q^{-2},y_F\sim-q^{-3}\)。
最后才作原扭曲
\((x_F,y_F)\mapsto(x_F/\theta_{17}^2,y_F/\theta_{17}^3)\)
到 R859 的目标 \(E_0\)。\(\theta_{17}\) 与全部原 Artin 系数同时运输。

作为无需开根的协变核对，若
$$
c_F=-T\,\frac{dv_F}{dT}
        +\frac{81-T}{2(T+27)}v_F,
$$
则 \(c_F=(D_QV-E_2V/2)/S^4\)。
这保持 R878 的完整第二项，不把普通导数代替协变导数。
(22)/(23) 使用的是原已认证曲线，不能单独由 characteristic-\(r\)
微分数据宣称存在。

## 8. 三条 \(P\) 共轭的同源消费公式

以下以 R870/R875 的完整特征零证书成功为前提；对 R880 中同一已认证 \(P\)，先使用 producer 的实际小目标
$$
C_{\rm new}:\quad Y^2+v_{\rm new}Y=X^3,\qquad
v_{\rm new}=\lambda(u)^3v.
$$
其 \(Y\) 是底 \(B\) 上由 R881 读取的函数 \(Y_P\)。
记
$$
R_P^3=\frac{Y_P(Y_P+v_{\rm new})}{(T+27)^2},\qquad
R_P(\infty)=1.
\tag{24}
$$
这是原坐标存在性和主项给出的完美三次幂。
对 endpoint \(i=0,2\)，把 (24) 及 \(Y_P\) 按 (17) pullback，
则
$$
X_{{\rm new},i}=B_{i,0}^{\,2}R_{P,i},\qquad
Y_{{\rm new},i}=Y_{P,i}.
\tag{25}
$$
令 \(d_{\rm new}=\lambda(u)h/2048\)，故 \(d_{\rm new}^3=v_{\rm new}/2\)；
目标 \(E_0\) 的完整坐标为
$$
\boxed{
\mathcal A_0q_i=
\left(
  \frac{B_{i,0}^{\,2}R_{P,i}}{d_{\rm new}^2},
  \frac{2Y_{P,i}}{v_{\rm new}}+1
\right).
}
\tag{26}
$$
其余两条按原 \(\widetilde\tau\) 共轭全部
\(v_{\rm new},d_{\rm new},Y_P,R_P\)。
底函数和两个 \(q_i\) 固定；系数的 \(\widetilde\tau\) 用 R864 的
实际 \(\ell,h^{\widetilde\tau}\)，不是另选范数根。
(26) 已显式保目标缩放，不需要把大数 \(\Xi_i\) 坐标另行重建。

## 9. 完整有限域求交的原输入

固定 \(r=29\)（若原剩余尺度需要，另用41），工作于原系数素位的
\(\mathbf F_{r^2}\)。实施顺序已经具体：

1. 由 (13) 构造并正规化原底函数域，保 Tate 地方和 (18)。
2. 在真实 \(L(mD_S)\) 中用 R881 的两个已认证 germ 读取
   \(Y_P,v_F\)；保其有限域换基和全部 cusp。
3. 用 (4)、(9) 的 degree18 base change、(14)/(15) 的全局一次 gcd，
   构造原源与两个 endpoint。
4. 按 (23)、(26) 读取同一 \(F,\mathcal A_rq_i\)，再用 R880 的两个
   三项 Fourier 矩阵，保全部九条原曲线。
5. 在 R859 的完整 pullback 除子
   \((\mathcal A_sq_2-\varphi_r\mathcal A_rq_0)^*[O]\)
   上取每个闭点的重数，推 \(F\) 并取完整剩余域迹；
   最后作原 point-only Artin 投影和所有既定尺度。

步骤5的除子不是“仿射两个坐标相等的不同点集合”。
特别 (7)、(14)、(15)、(21)、(26) 的分母零点必须用同一正规化地方的
赋值/延拓；表中三个特殊底值也不能省掉。
本篇没有执行该步骤，没有用所有可能点的扫描替代原闭点 divisor。

## 来源与独立性

- R831/R848：原群、真实 \(q_0/q_2/q_6\)、level 及完整返回尺度。
- R862/R864/R880：实际三次域、Artin 共轭和同次数三基。
- R870/R878/R881：两份原坐标证书及固定好素数直接读取。
- R859：原 shadow、正规化闭点迹和全部边界。

(3)–(17) 与 (20)–(26) 均为明确函数域/模函数恒等式；
没有新增数学数值执行、独立中央零或 canonical 类的比例假设。

## 附录 A：原底上的 degree48 eta 坐标及可判定的小模型分支

本附录保持正文的 \(T,U,V,Q\)，不改源曲线、两个 endpoint 或任一
Artin 系数。它把 RR 正规化可采用的有理底次数从306降到48；
尚不声称相应公开计算已经完成。

### A.1 真实模函数和完整 cusp 表

在 \(B=X_0(867)\) 定义
$$
t(Q)=
\frac{\eta(Q)\eta(Q^{867})}
     {\eta(Q^3)\eta(Q^{289})}
=Q^{24}(1+O(Q)).
\tag{A1}
$$
其 eta 指数在 \(1,3,289,867\) 分别为 \(1,-1,-1,1\)。
权为0，两项模24检验都是576，且
\(\prod d^{r_d}=867/(3\cdot289)=1\)。
因此 (A1) 是 \(\Gamma_0(867)\) 的 **trivial-character**
模函数；不存在待删的 eta multiplier。这里使用 Newman 的
eta-quotient 判据，及 Ligozat cusp 阶公式，见 Rouse–Webb,
*On spaces of modular forms spanned by eta-quotients*，作者稿印p2，
式(2)及其后 Theorem：
<https://users.wfu.edu/rouseja/cv/etaquos.pdf>。

直接从三个 eta 商相除，得到带首项规范的恒等式
$$
\boxed{t^{12}=T/V.}
\tag{A2}
$$
特别不是在某个新 Kummer cover 中另取十二次根。

对 cusp 分母 \(c\mid867\)，下表列每一个几何 cusp 上的阶。
“个数”是该分母类型的几何 cusp 数，不能在有限域只取有理点。

| \(c\) | 个数 | \(\operatorname{ord}T\) | \(\operatorname{ord}U\) | \(\operatorname{ord}V\) | \(\operatorname{ord}t\) |
|---:|---:|---:|---:|---:|---:|
| \(1\) | 1 | 289 | 17 | 1 | 24 |
| \(3\) | 1 | \(-289\) | \(-17\) | \(-1\) | \(-24\) |
| \(17\) | 16 | 1 | 17 | 1 | 0 |
| \(51\) | 16 | \(-1\) | \(-17\) | \(-1\) | 0 |
| \(289\) | 1 | 1 | 17 | 289 | \(-24\) |
| \(867\) | 1 | \(-1\) | \(-17\) | \(-289\) | 24 |

为核对该表，写 \(c=3^\epsilon17^j\)，\(j=0,1,2\)。
对 \(T_3(Q^{17^k})\)，Ligozat 式给
$$
\operatorname{ord}_{c}T_3(Q^{17^k})
=(-1)^\epsilon
17^{\,\max(2-2j,0)+2\min(j,k)-k}.
\tag{A3}
$$
再以 (A2) 除12即得最后一列。eta 在上半平面无零极，所以表已列出
\(t\) 的完整除子。四个非零阶 cusp 均为原有理 cusp，因此
$$
\boxed{
\operatorname{div}(t)=24([c_1]+[\infty]-[c_3]-[c_{289}]),
\qquad \deg(t:B\longrightarrow\mathbf P^1)=48.
}
\tag{A4}
$$
在 \(r=29,41\) 的原良好约化上，同一结论成立。
(A2) 保证零极仍仅在 cusp；各原 cusp 展开的首单位和上述阶保持。
且 \(t=Q^{24}(1+O(Q))\)、\(r\nmid24\)，故该 degree48 映射可分。

### A.2 小模型确实恢复整个原函数域

令 \(k=\mathbf Q\)、其系数扩域，或上述良好有限域。
正文(13)的非回溯塔给
$$
k(B)=k(T,U,V)=k(T,V);
\tag{A5}
$$
第二个等号也可由正文的 monic 一次 gcd 恢复 \(U\)。
由 \(t\in k(B)\) 和 \(V=T/t^{12}\) 得
$$
\boxed{k(B)=k(t,T),\qquad [k(t,T):k(t)]=48.}
\tag{A6}
$$
所以这不是只有 gonality 上界而没有原坐标的存在论。

具体设
$$
P(T,V)=
\frac{\operatorname{Res}_Z
  (\Phi_{17}^{(3)}(T,Z),\Phi_{17}^{(3)}(Z,V))}
 {(V-T)^{18}}.
\tag{A7}
$$
对 \(P(X,X/t^{12})\) 清 \(t\) 分母、去 \(k[t]\)-content 及纯 \(X\)
因子，得到 \(G(t,X)\)。在 \(k(t)[X]\) 分解 \(G\)。
原 \(T\) 的最小多项式是其中一个精确 degree48 因子
$$
F(t,X),\qquad F(t,T)=0.
\tag{A8}
$$
它在原常数域上定义，不要求为构造原模型而扩张到含 \(\mu_{12}\)。

给出一个有限、绝对的选支规则，避免任取某个 degree48 因子。
将每个不可约因子清分母为 \(k[t,X]\) 的 primitive 多项式。
给单项式 \(t^iX^j\) 权 \(24i-j\)，取最低权部分
\(\operatorname{in}_{24,-1}(F)\)。**原因子唯一满足**
$$
\operatorname{in}_{24,-1}(F)(1,1)=0.
\tag{A9}
$$
选出后仍核 \(\deg_XF=48\)，并在该分支按原
\(T=T_3(Q)\)、\(t=t(Q)\) 确定 Tate 地方。

证明唯一性如下。在 \(\bar k\) 上，(A7)加入 \(t^{12}=T/V\) 的
generic reduced 代数，因原 \(t\) 已在 \(k(B)\)，恰分解为12个原曲线
拷贝，分别给基坐标 \(t=\zeta\,t_{\rm orig}\)，\(\zeta\in\mu_{12}\)。
这些拷贝不能进一步混同：一个同时固定 \(T,V\) 的原函数域自同构
由 (A5) 必为恒等，因此不可能非平凡地改 \(t_{\rm orig}\) 的根单位。

在每个拷贝的 \(t=0\) 上，表中仅有两处：
一处 \(T\) 零阶289，另一处是原 \(\infty\)，
\(T\) 极阶1、\(t\) 零阶24。
后一处有
$$
tT^{24}\longrightarrow\zeta.
\tag{A10}
$$
相应极支 Newton 边因此是一个单项式乘
\(tX^{24}-\zeta\)；它的24个 Puiseux 首根无重，因为 \(r\nmid24\)。
常数域未代数闭时，一个不可约因子的该边为相应 Galois 轨道这些
因子的积。故 (A9) 当且仅当轨道含 \(\zeta=1\)。
该轨道只有1，恰给原 degree48 因子。这同时证明了
\(G\) 的 geometric 部分为12个互异的 degree48 因子，
而不是一个未知的高次场扩张。纯 \(t\) 或 \(X\) 的清分母因子
不参与选支。

### A.3 两个返回公式和原 RR 除子保持

在新域 \(k(t)[T]/(F)\) 中定义
$$
V=T/t^{12},\qquad
U=-[\text{常数项}]
\gcd_Z\bigl(\Phi_{17}^{(3)}(T,Z),\Phi_{17}^{(3)}(Z,V)\bigr),
\tag{A11}
$$
gcd 取 monic，一次性仍由原非回溯模问题保证。
这给 (A5)/(A6) 的实际双向函数域同构。

正规化后原 Tate 地方由
$$
\operatorname{ord}t=24,\quad
\operatorname{ord}T=-1,\quad
\operatorname{ord}U=-17,\quad
\operatorname{ord}V=-289,\quad
(tT^{24})(\infty)=1
\tag{A12}
$$
确定；其中 \(1/T\) 仍是该地方的 uniformizer。
正文的
$$
D_S=\operatorname{div}(dT/T)+\sum_{\rm all\ cusps}[c]
\tag{A13}
$$
完全不变，仍为次数204的有效除子。
全部36个 cusp 由 \(T\) 的零极完整恢复；\(t\) 的四点支撑
**不能**替代这个 cusp 和。

随后正文(14)–(17)的 level9 gcd、两个原 endpoint、
(21)的 \(\varepsilon\) 及(23)/(26)的两坐标全部原样读取。
没有丢失 \(q_0/q_2\)、任何分母零点或原三 Artin 共轭。

实现时，newfield 的元素写为
\(\sum_{i=0}^{47}a_i(t)T^i\)。
其 Tate 代入的逐项低阶是
$$
24\,\operatorname{ord}_{t=0}a_i-i,
\tag{A14}
$$
可据此严格预付每个 Laurent 取消所需精度。
这直接消费两份原已认证 germ；不把特征 \(r\) 的微分唯一性
当成映射存在性。

本附录给出了原 degree48 模型的有限因子生成和绝对选支程序。
它没有报告一次尚未执行的 factorization 或 RR 运行为成功，
也没有断言任一 shadow 非零。第一版 degree306 公开运行不因本附录而
被默认为错误；两者正规化的是同一条原曲线和同一除子。

## 附录 B：原 eta 的 Fricke 商、degree24 底与完整 RR 分解

本节继续使用附录A的同一个
$$
B=X_0(867),\qquad
T=T_3(Q),\quad U=T_3(Q^{17}),\quad V=T_3(Q^{289}),\quad
t=\frac{\eta(z)\eta(867z)}{\eta(3z)\eta(289z)},\quad Q=e^{2\pi iz}.
$$
原 \(U\) 始终表示中间17端点。下面新的商坐标记作 \(J\)，不覆盖这个 \(U\)。
本节的 Fricke 对合 \(W=w_{867}\) 作用在底曲线 \(B\)；
它与R883交换两个2端点的源对合不是同一个算子。
以下给完整符号证明，没有执行新的因子分解或RR计算。

### B.1 同一个 eta 商在 Fricke 下不变

由 \(\eta(-1/z)=\sqrt{-iz}\eta(z)\)，在 \(z\mapsto-1/(867z)\) 下四个 eta 因子两两交换。
平方根倍率在分子、分母均为同一个 \(\sqrt{867}(-iz)\)，故
$$
\boxed{
W(t)=t,\quad W(T)=\frac{3^6}{V},\quad
W(V)=\frac{3^6}{T},\quad W(U)=\frac{3^6}{U}.
}
\tag{B1}
$$
取正虚轴可先逐项固定平方根和eta的正实值，然后由解析延拓得到全恒等式；
这里没有留下一个未定的十二阶单位。
又原 \(t^{12}=T/V\)，所以令
$$
a=3^6t^{12},\qquad
J=T+\frac aT=T+\frac{3^6}{V},\qquad
w=T-\frac aT
$$
便有
$$
\boxed{
W(J)=J,\quad W(w)=-w,\quad
w^2=J^2-4a,\quad T=\frac{J+w}{2},\quad V=\frac{T}{t^{12}}.
}
\tag{B2}
$$
原中间 \(U\) 仍用正文的两个17多项式的一次gcd恢复；没有另选端点。

附录A已付 \(k(B)=k(t,T)\)、\([k(B):k(t)]=48\)。
在原无穷分支，
$$
t=Q^{24}(1+O(Q)),\quad T=Q^{-1}(1+O(Q)),\quad
3^6/V=3^6Q^{289}(1+O(Q)),
$$
所以 \(W(T)\ne T\)。由(B2)，\(T\) 在 \(k(t,J)\) 上满足真正的二次方程
$$
T^2-JT+a=0.
$$
因此固定域和次数准确为
$$
\boxed{
k(B)^W=k(t,J)=k(B^+),\quad B^+=X_0(867)/\langle W\rangle,\qquad
[k(B^+):k(t)]=24.
}
\tag{B3}
$$
这保留了整个原 \(B\) 作为二次扩张；没有把所需映射强行下降到 \(B^+\)。
返回原分支时须取
$$
\boxed{w=Q^{-1}(1+O(Q)),\quad T=(J+w)/2,}
\tag{B4}
$$
不是任选一个平方根。

### B.2 二十四个分歧点、属三十七和十八个 cusp

给出本数值的直接计数，避免将非极大序的类数误作同一个二次域类数。
Fricke作用及商的标准定义可参见
[Maier, *Algebraic hypergeometric transformations of modular origin*, §2, (2.2)](https://www.ams.org/journals/tran/2007-359-08/S0002-9947-07-04128-1/S0002-9947-07-04128-1.pdf)。
这里的固定点数用下述原 \(N=867\) 的整环计算支付。

一个非cusp Fricke固定点给一个循环 \(N\) 同源的自对偶类。
在上半平面表示中，\(\gamma w_N\) 的迹是 \(N\) 的整数倍；
其固定点在上半平面使该矩阵椭圆，故迹的绝对值小于 \(2\sqrt N\)。
因 \(N>4\)，该迹必为零。相应CM自同源 \(\alpha\) 满足
$$
\alpha^2=-867,\qquad \alpha=17\sqrt{-3}.
$$
于是其端环是包含 \(\mathbf Z[\alpha]\) 的
\(K=\mathbf Q(\sqrt{-3})\) 的序。写
\(\mathcal O_K=\mathbf Z[\omega]\)、\(\sqrt{-3}=1+2\omega\)，
则 \(\mathbf Z[\alpha]\) 的导子为34。
可能的端序导子是 \(1,2,17,34\)。

导子1或2时，\(\sqrt{-3}\) 已在端环，故
\(\alpha\in17\operatorname{End}(E)\)，其核包含全部 \(E[17]\)，不是循环。
导子17或34时，\(\alpha/17=\sqrt{-3}\) 不在该端环，故核不含 \(E[17]\)；
因 \(\deg\alpha=3\cdot17^2\)，这正好保证核循环。
这两类序的单位只有 \(\{\pm1\}\)，两个符号的 \(\alpha\) 给同一个核。
每个相应的真理想类给一个固定点，反向也按上述自同源恢复，故点数为这两个序的类数之和。

\(\mathcal O_K\) 为欧氏环、类数一。其非极大序的类群由
$$
(\mathcal O_K/f\mathcal O_K)^\times/
\bigl((\mathbf Z/f\mathbf Z)^\times\mathcal O_K^\times\bigr)
$$
准确给出。
17在 \(K\) 惰性，故 \(f=17\) 时分子阶288，两个分母子群的阶为16和6、交为阶2，
所以类数为 \(288/48=6\)。
2亦惰性，\(f=34\) 时CRT给分子阶 \(3\cdot288=864\)，分母仍为阶48，
所以类数为18。于是
$$
\boxed{\deg\operatorname{Ram}(B/B^+)=6+18=24.}
\tag{B5}
$$
这是几何点总数／闭点次数和，不把它们都认成 \(\mathbf F_r\) 或 \(\mathbf F_{r^2}\) 有理点。

原 \(B\) 的属85已在正文支付。由Riemann–Hurwitz，
$$
168=2(2g(B^+)-2)+24,\qquad
\boxed{g(B^+)=37.}
\tag{B6}
$$
Fricke将cusp分母 \(d\) 交换为 \(867/d\)。
867不是平方数，故36个原cusp无一个固定，组成18对。
记两层的约化cusp除子为 \(\mathcal C_B,\mathcal C_+\)，则
$$
\boxed{\deg\mathcal C_+=18,\qquad \pi^*\mathcal C_+=\mathcal C_B.}
\tag{B7}
$$
原 \(t\) 的两个零cusp \(c_1,\infty\) 互换，两个极cusp \(c_3,c_{289}\) 互换；
故在 \(B^+\) 上 \(t\) 恰有一个24阶零cusp和一个24阶极cusp。
这些都保原绝对eta，不增加新分支。

在所用 \(r=29,41\) 上，模曲线及cusp在良约化内，且2可逆。
非平凡对合的固定点局部切向作用为 \(-1\)，故固定概形在这些良约化上保完整24次；
(B5)–(B7)相应保持。没有以仿射判别式的裸零点数替代正规化的分歧除子。

### B.3 一个真正 Fricke 不变的 weight2 分母

原分母 \(S=-D_Q\log T\) 的除子不必在 \(W\) 下不变。
不能直接把旧 \(D_S\) 的RR空间按(B2)强行拆开。
改用明确的同权模形式
$$
S_t=\frac1{24}D_Q\log t,\qquad S_t(\infty)=1,
$$
并定义真正的几何除子
$$
D_t=\operatorname{div}_B(dt/t)+\mathcal C_B,\qquad
D_+=\operatorname{div}_{B^+}(dt/t)+\mathcal C_+.
$$
因 \(t\) 是模单位，两个对数微分仅在cusp有至多简单极；
\(dt/t\ne0\)，在原无穷cusp的留数24为所用特征的单位。
因此两除子均有效，且
$$
\boxed{
\deg D_t=204,\quad \deg D_+=90,\quad
D_t=\pi^*D_++\operatorname{Ram}(B/B^+).
}
\tag{B8}
$$
最后一式是完整可分微分拉回公式及(B7)，所以包括全部ramification和cusp。
在原无穷cusp \(D_t\) 的系数为零。

与旧RR输入的转换有一个固定的真实乘子：
$$
\boxed{
a_t=\frac{S_t}{S}=-\frac{T}{24t\,dT/dt},\qquad
L(mD_t)\ \xrightarrow{\ f\mapsto a_t^m f\ }\ L(mD_S).
}
\tag{B9}
$$
这里 \(dT/dt\) 是同一原函数域的导数，非零由原T的cusp阶保证。
确实 \(\operatorname{div}(a_t)=D_t-D_S\)，故
\(\operatorname{div}(a_t^mf)+mD_S=\operatorname{div}(f)+mD_t\)。
这同时保全部有限极与原 \(\infty\) 的首项；
(B9)方向不能倒写。所有原M2乘积、低核、17端点及Artin尺度均可在转换后原样读取。

### B.4 属三十七上的两个真 RR 空间

令
$$
\delta_J=J^2-4a\in k(B^+)^\times,\qquad
\operatorname{div}(\delta_J)=2A+\mathcal B,
$$
其中每个赋值按 \(2a_Q+b_Q\)、\(b_Q\in\{0,1\}\) 唯一拆分。
\(\mathcal B\) 是二次扩张 \(w^2=\delta_J\) 的约化分歧底除子，允许原有极点给奇赋值；
\(\deg\mathcal B=24\)、\(\deg A=-12\)。
这里必须在正规化上求完整除子，不先将判别式多项式的有限平方因子略去。

对任意整数 \(m\ge1\)，有准确的原函数直和
$$
\boxed{
\begin{aligned}
L_B(mD_t)
={}&L_{B^+}\!\left(mD_++\left\lfloor\frac m2\right\rfloor\mathcal B\right)\\
&\ \oplus\
w\,L_{B^+}\!\left(mD_++A+
        \left\lfloor\frac{m+1}{2}\right\rfloor\mathcal B\right).
\end{aligned}}
\tag{B10}
$$
证明只需逐闭点检查。对非分歧点，\(w\) 的阶为 \(a_Q\)；
对分歧点，其上唯一点满足
\(\operatorname{ord}(w)=2a_Q+1\)、\(\operatorname{ord}(\pi^*f)=2\operatorname{ord}_Q f\)。
允许 \(m\operatorname{Ram}\) 的极时，不变项恰能有
\(\lfloor m/2\rfloor\) 倍 \(\mathcal B\) 的底极；
反变项 \(w f\) 恰要求
\(\operatorname{ord}_Q f\ge-a_Q-\lfloor(m+1)/2\rfloor\)。
再加同一个 \(mD_+\) 即得(B10)。
因2为单位，不变／反变投影保该完整 \(W\)-稳定极除子，二者不会靠互相取消极点扩充空间。

(B10)两除子的次数分别为 \(102m\) 和 \(102m-12\)，奇偶只交换其归属。
二者对 \(m\ge1\) 都大于 \(2g(B^+)-2=72\)，所以Riemann–Roch给维数
$$
\boxed{\{102m-36,\ 102m-48\},\qquad
\dim L_B(mD_t)=204m-84.}
\tag{B11}
$$
特别原weight2基可由
$$
\boxed{54\ \text{个不变基函数}+66\ \text{个反变基函数}=120}
\tag{B12}
$$
完整构成。不是只选一个Fricke符号；原两种符号及全部M2都在(B10)内。
之后按(B9)返回原 \(D_S\) 即为原坐标消费者所需的同一空间。

### B.5 原 resultant 可先降为 degree288 再选原 degree24 因子

附录A从原非回退17关系得到的 \(R_t(X)\) 在去掉content和纯 \(X\) 因子后，
在 \(k(t)\) 上归一为首一degree576。
其十二个几何eta副本分别由(B1)保留，且每个degree48副本的根被
\(X\mapsto a/X\) 两两配对。
因此完整首一多项式准确满足
$$
\boxed{X^{576}R_t(a/X)=a^{288}R_t(X).}
\tag{B13}
$$
定义
$$
C_0(J)=2,\quad C_1(J)=J,\quad
C_n(J)=JC_{n-1}(J)-aC_{n-2}(J).
$$
由递推 \(C_n(X+a/X)=X^n+a^nX^{-n}\)。
若 \(R_t(X)=\sum_{i=0}^{576}r_iX^i\)，则(B13)的系数关系给
$$
\boxed{
X^{-288}R_t(X)=Q_t(X+a/X),\qquad
Q_t(J)=r_{288}+\sum_{n=1}^{288}r_{288+n}C_n(J).
}
\tag{B14}
$$
这是原whole resultant的恒等式，不是截短其系数。
(B3)表明所需原商的因子degree24。
它仍由同一个绝对分支
$$
t=Q^{24}(1+O(Q)),\qquad J=Q^{-1}(1+O(Q))
$$
即最低权 \(\operatorname{wt}(t)=24,\operatorname{wt}(J)=-1\)、
首项 \((1,1)\) 选定；原eta的其余相位继续保在其它因子中。
回原域再用(B4)，故没有因二次商丢掉原无穷分支。

这给原RR前端一个精确degree24加二次返回的实现路径；
当前已有degree306和eta48运行不因本符号结论被认作成功或失败。
实际执行仍须付原因子、正规化、全部除子及(B9)转换的完整输入，
本节没有给任何一张未认证映射补上PASS，也没有预报原shadow的非零。
