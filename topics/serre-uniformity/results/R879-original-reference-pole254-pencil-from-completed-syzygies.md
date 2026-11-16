# R879 — 从已成418条配对关系得到参考单极函数与九范数铅笔

日期：2026-11-16。状态：本文给出已成 R872 来源上的新有限消费者；本文没有执行新的线性代数，也没有把下面的291阶子式预填为非零。原曲线、点、框架与 Hecke 对应全部保持。

## 1. 已成来源与本次唯一新目标

[R876](../results/R876-original-nine-norm-generators-and-rigidified-Hecke-ideals.md) 的参考线丛为
$
M_0=\mathcal O_Y(254P_0),\qquad g(Y)=127.
$
只要构造一个原函数
$
(v_0)_\infty=254P_0,                                      \tag{RP.1}
$
则截面 $1,v_0$ 已是 $M_0$ 的无基点铅笔：1在 $P_0$ 外处处非零，而 $v_0$ 在
$P_0$ 的线丛纤维非零。本参考因子因此不必先取得128个截面或另做 R876 的672阶铅笔子式。

实际 [R872 成功结果](../results/R872-certified-original-P0-jets-and-fixed-Picard-spaces.md)
来自 run43830071469、source a07453ec81e832b0aeef99bded2efaa763adaf13。
其 genus127、$\deg H=272$、原正常基次数
$\epsilon=(0,1^{144},2^{127})$ 与原 $\tau,\sigma$ 均不改。
实际单位素点是 $1000000753$，原 $K=\mathbf Q(\zeta)$ 的根为549966761。
该已成源给出两个准确的、未要求展开系数的截面
$
u,b\in V_2=H^0(2H),\qquad
\min(\operatorname{div}_{2H}u,\operatorname{div}_{2H}b)=272P_0,
$
$
\operatorname{div}_{2H}u=272P_0+D_\chi,\quad
\deg D_\chi=272,\quad P_0\notin D_\chi.                    \tag{RP.2}
$
这不是仅由两个模向量猜测的共同零。R872 的真962阶铅笔子式、完整乘法核与已证明的
Koszul 维数给出了原特征零的 (RP.2)。

R872 同时给原 $V_3$ 坐标下的两矩阵
$
S,T:K^{418}\longrightarrow V_3,\qquad u\,T(c)+b\,S(c)=0, \tag{RP.3}
$
且 $S$ 将 $K^{418}$ 同构到完整 $H^0(3H-D_\chi)$。
每个矩阵的准确系数以原已认证的单位线性系统定义；保存的有限域数组是这些准确系数在
同一合法素点的实际约化，不能将它们改称重构的特征零数组。

本次不重新计算原点 jets、146核、u/b、任何旧乘法、690逆、272逆或418核。

## 2. 两个最高次数截断恰给完整 H0(272P0)

原 $V_m/\tau^m$ 的正常基顺序为
$
\mathcal V_m=\{z^a\beta_i: i=0,\ldots,271,\ 0\le a\le m-\epsilon_i\}.
$
原 $\tau:V_2\hookrightarrow V_3$ 在这个表示中就是相同多项式的包含。
所以一个 $V_3$ 列属于 $\tau V_2$，当且仅当每个正常行的最高项
$z^{3-\epsilon_i}\beta_i$ 的系数为零。共有272条条件，不另乘 $82^2$。

令 $E$ 抽出上述272行，并形成
$
L=\begin{pmatrix}ES\\ET\end{pmatrix}:K^{418}\longrightarrow K^{544}. \tag{RP.4}
$
两块都必须保留。只截 $S$ 不能据此排除 $\tau=0$ 上的额外极点。

对 $c\in\ker L$，存在唯一 $f,g\in V_2$ 使
$
S(c)=\tau f,\qquad T(c)=\tau g.
$
由原曲线整性和 (RP.3) 可消去 $\tau$，得到
$
ug+bf=0,\qquad h=f/u=-g/b.                              \tag{RP.5}
$
在任意点取同一个 $2H$ 的局部平凡化。$f,g$ 都是局部正则截面，于是
$
\operatorname{ord}_Q h\ge
-\min(\operatorname{ord}_Q u,\operatorname{ord}_Q b)
=-272\,1_{Q=P_0}.
$
故 $h\in H^0(272P_0)$，没有在 $\tau$ 零点或 $D_\chi$ 上漏极点。

反之，对任意 $h\in H^0(272P_0)$，由 (RP.2) 得
$f=hu,\ g=-hb\in V_2$。配对 $(\tau f,\tau g)$ 属于 (RP.3) 的完整核。
其 $S$ 坐标唯一，故对应唯一 $c\in\ker L$。因此
$
\boxed{\ker L\simeq H^0(272P_0),\qquad c\longmapsto f/u.} \tag{RP.6}
$
这是真正函数的同构，保留原分子、分母和符号，不只是 Picard 类相等。
RR 给 $h^0(272P_0)=146$，所以准确 $\operatorname{rank}L=272$。

特别地，常数函数1对应 $(f,g)=(u,-b)$。无需另外求这个列，也不把它的存在当成未知
参考128空间已完成的声称。

## 3. 十九个已成局部系数只新选一个函数

R872 的实际局部参数记为 $x$，它是真正 $z-z_0$ 或 $w-w_0$，不是未核的形式支。
原点处 $\tau\ne0$，R872 已保存
$
J_n(f)=[x^n](f/\tau^2),\quad n=0,\ldots,272
$
在全部418个原 $V_2$ 基列上的矩阵。对已经满足 $Lc=0$ 的列，将 $S(c)$ 的
低次系数读作 $f$ 的原 $V_2$ 坐标即可。记这个418行抽取矩阵为 $S_{\rm low}$，
不改原列尺度。

新增系统为
$
\mathcal A c=
\begin{pmatrix}
ES\\ ET\\ J_0S_{\rm low}\\ \vdots\\ J_{18}S_{\rm low}
\end{pmatrix}c
=
\begin{pmatrix}0_{562}\\1\end{pmatrix}.
\tag{RP.7}
$
它有563行、418列，前544行为 (RP.4)，随后18个零条件以及第18阶归一条件。

在 (RP.6) 下，要求 $J_0,\ldots,J_{17}$ 为零恰是
$h\in H^0(254P_0)$，再要求 $J_{18}=0$ 恰是 $h\in H^0(253P_0)$，因为
$u/\tau^2$ 在 $P_0$ 的阶恰为272，且其第272阶系数 $U_{272}\ne0$。
RR 准确给
$
h^0(254P_0)=128,\qquad h^0(253P_0)=127.
$
所以十九条系数在 $\ker L$ 上满秩19，且第18阶可以归一为1：
$
\boxed{\operatorname{rank}\mathcal A=291,\quad
\mathcal A c=(0,\ldots,0,1)^t\ \text{在准确原域上可解}.}
\tag{RP.8}
$

实际消费者只需从真实约化中选择291行、291列的单位子式。按原行列顺序选择，未选
127个坐标置零；所选坐标由这一原准确方阵与选中右端唯一确定。
非零模子式证明原分母在该素点为单位；(RP.8) 保证所选行的准确解满足全部563行，
并且实际有限域实现仍须完整乘回全部563行。不能仅核所选291行。

得到 $f,g$ 后，定义
$
v_0=\frac{f/\tau^2}{u/\tau^2}=\frac fu.
\tag{RP.9}
$
式 (RP.6) 排除了所有非 $P_0$ 极点；第18阶归一和 $U_{272}\ne0$ 给
$
v_0=U_{272}^{-1}x^{-254}(1+O(x)),
$
从而准确得到 (RP.1)，不是只得到“极阶至多254”。
若当前剩余域未得到291秩，本次只记录充分检验未通过；不据此否定 (RP.8)，不替换原曲线。

## 4. 原 M0 铅笔与尚未物化的 t 框架单位

在 $M_0=\mathcal O(254P_0)$ 内，截面1的除子为254P0，而截面 $v_0$ 在 P0 的纤维非零。
故
$
\boxed{(1,v_0)\text{ 全局生成 }M_0.}                     \tag{RP.10}
$
这直接满足 R876 九范数定理的参考输入，不再执行该参考的672阶铅笔检验，
不构造参考128基，不重复旧146或418的核。

原 YP 框架仍是 $t^{-254}$，其中 $t=a^3$。若原准确参数关系为
$t=c\,x+O(x^2)$，则此框架下
$
(v_0)_{P_0}=c^{254}/U_{272}.                            \tag{RP.11}
$
这里只给出准确来源表达式，不能把 $c$ 设成1或把 $x$ 改名为 $t$。
R872 的本次成功没有求完 $t(x)$，因此本消费者的
original_t_frame_scalar_expanded 必须为 false。它不妨碍 (RP.10) 或参考范数理想生成，
但后续实际刚性化/非 $p$ 比较仍须消费 (RP.11) 的真参数来源或完整 Artin 纤维框架。

此铅笔可先在原 $K=\mathbf Q(\zeta)$ 上选取；不能因为模系数是整数代表就宣称 $v_0$
单独在 $\mathbf Q$ 上定义。参考线丛本身在 $\mathbf Q$ 上定义，(RP.10) 在 K 上生成
及其忠实平坦下降足以标识同一个参考理想；后续原 $-3$ 下降和 R876 的对应方向仍保留。

## 5. 实际字段、所需选件和来源边界

原 R872 文件不是本次改标签的新 stage：

|用途|原文件及字段|
|---|---|
|两组690×418配对矩阵|R872-pencil-trial-000001-complete-fixed-chi-kernel.json.gz 的 V3_kernel_basis_mod_prime、paired_u_multiplier_coordinates_mod_prime|
|273×418原局部系数|R872-V2-original-point-jet-matrix.json.gz 的 matrix_mod_prime、V2_basis、row_orders|
|分母 u 与原第272阶|R872-anchor-u.json.gz 的 V2_coordinates_mod_prime、exact_order272_unit、exact_section_definition|
|共同零与准确配对来源|原完整418核的 divisor_definition、exact_kernel_definition 和全部完整关系旗标|
|原点、参数和素点|原 source-audit、point-linearization、最终证书及配置|

完整418核为2798517字节/SHA256
250489e7a5a37b52527b44fee79354d7e916eb1243079ffd656d143d40398324；
jet矩阵为581694字节/SHA256
025a29fed69d8575c757454309bad6fca3198457a967d5ed88766d83f82d2ec7；
原 u 为7216字节/SHA256
f74b130ccff9f4c1cccc8098e49b9bb315487a4b8b41627e3ba6c488b726ef97。
它们都在已结束原 artifact14207558653 中，原 manifest 为
5001e5be47484c649a28afb82c89cf95995f0a3a0d05498173bbb680451cbb80。

最小新算术不读取原122MB输入包、不读取全部272阶的单阶文件、不重新求任何旧逆。
原最终证书、完整来源配置、全 manifest 和实际被读的旧 stage 原字节一并保留。
准确特征零叶是 R872 已认证的旧 unit-solve 表达式；本次有限域数组不是它们的替代。
如后继需要展开或逐算这些旧特征零表达式，必须另消费其真实依赖闭包，不能仅凭
本次小包声称原 W/所有旧矩阵已经再展开。

本次可保原 u/b 的小元数据与原完整146核，用于检查 u 的规范方向与源关系；
不重新执行那个核。所有未读的大依赖在新来源审计中明确为认证外部叶，不伪称已重新哈希。

## 6. 实际 Actions 消费与准确完成出口

新 core 的数学 RESULT 为 R879-original-reference-pole254-pencil。
新源码、本文、原 R876/R872 证明、原成功 producer/manifest/选件、原素点及全部矩阵顺序
都进入新的数学 tag。旧 R872 stage 保旧 tag，绝不重新封为本次运算。

依次原子保存：

1. 来源/schema 审计、旧矩阵与原基顺序的相符性；
2. (RP.7) 的真实563×418矩阵和原行/列含义；
3. 实际291阶单位子式、两侧逆乘回、唯一自由零解以及全部563行乘回；
4. 原 $V_2$ 分子 f、配对 g、分母 u 的实际模坐标和准确 unit-solve 源；
5. 参考铅笔 $(1,v_0)$、唯一极点/极阶证书和 (RP.11) 的未展开框架表达式。

全部这些新矩阵、向量、机器证书只在公开 Actions 和一日 artifact 内。
预算或硬中断恢复只读同 tag 已完成 stage，不重旧 R872 算术，也不重本次已提交的矩阵。
成功出口要求实际291子式非零、完整563行残差为零、原 u 的第272阶非零，
并保全部 (RP.2)–(RP.9) 的原全局来源。有限域消元自身不是特征零系数重构。

成功时可准确声明：原参考 $M_0$ 的一条源绑定单极函数和无基点铅笔已认证。
五个原 $M_j$ 的128截面、参考九范数的实际8×8行列式、循环7在原 Picard 类上的作用、
活跃谱支持、主函数校准、Poincare period、非 $p$ 项和高度，均不由本消费者宣称完成。
