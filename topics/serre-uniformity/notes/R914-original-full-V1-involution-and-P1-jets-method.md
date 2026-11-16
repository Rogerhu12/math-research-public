# R914：完整原 V1 几何反射与 P1 局部展开的最小执行契约

日期：2026-11-16。状态：执行方案与完整消费者源码；本文件不预填尚未运行的矩阵或展开结果。新算术仅在本公开仓库 GitHub Actions 内执行。

理论入口是 [R912](../results/R912-original-eight-dimensional-endpoint-lattices-and-norm-frames.md) §2，SHA256
$\texttt{273ef827c365b7901f349150f0665cffd57e330e2806dd8113649b3482671e97}$。
本次只关闭完整几何 $\iota$ 和真正 $P_1$ 局部源。八维整端点代数、九范数端点值、$\operatorname{Nm}(q^*\Phi)\det U$、两端刚性化及高度均不在本次完成标志内。

## 1. 同一原对象与两种作用

令 $K=\mathbb Q(\zeta)=\mathbb Q(s)$，$\zeta=(-1+s)/2,\ s^2=-3$。原几何作用
$$
\iota=T^{41}:Y_K\longrightarrow Y_K
$$
是 $K$-线性的。原 R802 的同一 cusp 与偶权 automorphy 因子给
$$
q_Y\longmapsto-q_Y,\qquad \iota^*t=1-t.
$$
本次不把 $s$ 或其他常数取共轭；算术 $c_Y$ 的半线性系数作用仍另行保留。

原146个截面是
$$
e_i=82^2T_{1,i}\quad(0\leq i<146).
$$
它们在 R786 文件中已经含整数尺度 $6724$。消费者直接读取该原数组，不再乘除 $82^2$。原标记截面及正常函数始终为
$$
\tau=e_0,\quad \sigma=e_1+e_{73},\quad w_0=e_2,\qquad
z=\sigma/\tau,\quad w=w_0/\tau,\quad\beta_{72}=e_{73}/\tau.
$$
这里 e73 既是原 V1 列，又给正常基第72行；两者只转换一次。

## 2. 只新增143个准确右端

原 $S\in\mathbb Z^{560\times146}$ 的行号为 $40n+r$，$0\leq n\leq13,\ 0\leq r<40$。它包含完整40个 $\xi_{41}$ 坐标，绝不改成280个 compressed 行。令
$$
D_{40n+r,40n+r}=(-1)^n .
$$
直接读取 R837 已认证的146个原选行 $J$ 及其真实非零子式见证。旧子式的见证素数不同于本次展开素数，不搬用那个素数的逆。

R853 已完整准确算出 $\iota^*\tau,\iota^*\sigma,\iota^*w_0$ 的三个有理坐标列。由于原 $e_i$ 的系数在 R802 所指定的额外常数共轭下固定，这三个旧算术共轭答案就是这三个特定原截面的几何答案；本次不推广这个说明去删除任意 $K$ 系数的共轭。

新 RHS 索引固定为
$$
\mathcal J=\{0,\ldots,145\}\setminus\{0,2,73\}.
$$
一次以有理算术求
$$
S_J C_{\mathcal J}=D_JS_{J,\mathcal J}.
$$
这正好143个新右端。旧三个目标不重新求解。填回
$$
C_{:,0}=C_\tau^{\rm old},\qquad
C_{:,2}=C_{w_0}^{\rm old},\qquad
C_{:,73}=C_\sigma^{\rm old}-C_{:,1}.
$$
于是得到完整 $146\times146$ 的准确有理矩阵。最后一式的减号来自原 $\sigma=e_1+e_{73}$，不是把 $\sigma$ 当作第1列。

选行系统先完整乘回；随后在原560行准确核
$$
SC=DS,\qquad C^2=I_{146},
$$
并核旧三列、$\tau$ 和 $w_0$ 的准确固定性。原 Fourier 评价的单射和 R802 的真实作用确定整个 V1 作用，不从有限域中矩阵平方为一猜测几何 involution。

准确矩阵存有理数分子/分母两字符串。它不是仅有一个 adjugate 表达式，也不是把有限域数组改标成有理矩阵。旧子式已证明 $S_J$ 在特征零非奇异，因此不新增一次大 determinant 或 rank 计算。

## 3. 指定原素点与完整旧展开

只在同一辅助素点
$$
\ell=1000000753,\qquad \zeta=549966761,\qquad s=99932770
$$
求新准确矩阵的约化。每个准确有理分母须实际为单位；若有非单位，保存已经完成的准确矩阵及全部来源，以 UnitFailure 如实停止。不会把失败改称几何作用不存在，也不会私换素点去混用原 jets。

R872 已成的273个原阶 $0,\ldots,272$ 逐文件读取。其真实参数字段是
$$
\texttt{chosen\_local\_parameter}=\texttt{z\_minus\_z0},
$$
点展开 index 则使用 $\texttt{local\_parameter}$。这两个原字段不互换。每个阶同时核原配置、原 point-linearization、上一阶 reference、272个正常坐标及原完整方程真旗标。

旧正常基按照原 R805 给
$$
e_0/\tau=1,\qquad e_1/\tau=z-\beta_{72},\qquad
e_i/\tau=\beta_{i-1}\ (2\leq i\leq145).
$$
因此从原272函数展开得到原 V1/tau 行 $E_0(\rho_0)$，只做这一原线性组合，不重旧 Hensel 递推、旧271阶逆、W、Mg 或 Gamma。

## 4. P1 参数与全部正常函数的运输

保持
$$
P_1=\iota(P_0),\qquad
\rho_0=z-z_0,\qquad
\rho_1=\iota^*\rho_0=z-2\beta_{72}-z_0 .
$$
本次绝不使用 $z-z(P_1)$ 代替 $\rho_1$。因为 $\iota^*\tau=\tau$，在这两个匹配参数下
$$
E_1(\rho_1)=E_0(\rho_0)C .
$$
将273行整体右乘准确矩阵的合法约化，完整核再右乘 $C$ 回到原 P0 行。同时核 $\tau,w_0$ 固定及 $\iota^*z=z-2\beta_{72}$。

正常基的前145个函数是 $1,e_2/\tau,\ldots,e_{145}/\tau$。后127个由 **原 R805 free-basis 文件实际保存的两 M2 叶 recipe** 给出。用新 P1 V1 展开作相应两因子截断乘法，保原列序和整数尺度。不另造正常基，也不构造另一个完整272阶半线性作用矩阵。

正常函数按16列一组原子保存，最后组为256..271，合17组。每组包含273行及真实原 M2 叶索引。完整 index 只在全部272列完成后写出。正阶特征零系数仍是“原 R872 Hensel 准确表达式 → 完整准确 C → 原 recipe”的确定表达；有限域数不标作已重构有理系数。

原 R837 的 $P_0/P_1$ 146个准确 CM 值另作必要零阶匹配。先在 $K$ 中以同一原 $\tau$ 值除去共同 frame，再合法约化，而不是分别约化可能带共同分母的未归一化 CM 值。核两份146坐标与旧/新展开常数项，并在准确 $K$ 中核 $P_0$ 行乘 $C$ 等于原 $P_1$ 行。后127个正常值沿同一 recipe 给出，作为全部272个新展开常数项的原点来源。

## 5. 原 t 帧只作真实运输

R883 已准确绑定
$$
t=c_0\rho_0+O(\rho_0^2),\qquad
c_0=\frac{a_1b_0-a_0b_1}{48s\,b_0^2},
$$
并在本素点认证 $c_0\ne0$。由真实 $\iota^*t=1-t$，
$$
t_1:=t-1=-c_0\rho_1+O(\rho_1^2),\qquad c_1=-c_0.
$$
本次只将原 R883 已成的三项取负，保存准确 unary-negation DAG 和原 expression；不再评价 N692/N693，不再求 CM 常数，不将一个模数称为展开的特征零常数。

完整正常展开有273项，原 t 帧已成展开只有3项。两个精度字段必须分别保留。程序还在新273项上核 $\rho_1$ 恰等于所用局部形式参数。

若原函数首项为 $L\rho_1^m$，运输到原 $t_1$ 帧是
$$
L\rho_1^m=(Lc_1^{-m})t_1^m(1+O(t_1)).
$$
负阶对应正乘 $c_1^{-m}$。不得省掉负号、LC 或原帧，也不预计算未来具体函数的 determinant 线丛校准值。

## 6. 真实最小来源与跨载体继承

本次只有六组原生产者，实际直接选择 **469** 个原成员。该计数不含运输用外层 manifest/inventory 的副本，也不更改旧 producer 的选择计数。

| 原组 | 直接数学所需的原成员 | 选择数 |
|---|---|---:|
| R786 | 146个原 power1 rows；原完成证书、stage index 和 metadata | 152 |
| R805 | 原 accepted pencil、graded free basis、完成证书和 metadata | 7 |
| R837 | 原 reflection minor/attempt、准确 P0/P1 CM 值、完成证书、stage index 和 metadata | 9 |
| R853 | 原三个准确坐标、source audit、function DAG、stage index、完成证书和 metadata | 9 |
| R872 | 原273个 jets、point-linearization、jet index、source audit、完成证书、完整 stage index 和 metadata | 282 |
| R883 | 五个已成小阶段、完成证书和 metadata | 10 |

R853 的原169成员载体含 R786152 和 R8378，可直接抽取这些原字节。R837 的准确 P0/P1 21 KB 记录已在真实 R856 的原569成员载体的 R837 组中；将这份原记录与 R853 载体中的 reflection 记录合并，得到所需九件，并逐字核共同 metadata。R805 free-basis **不在 R853 载体内**；它也从上述 R856 载体抽取原 R8057件。两个载体都逐成员核 bytes/SHA，保原 producer metadata，不改原 source tag，不再访问旧 R837 平台产物。

R872 的273阶和 R883 五小阶段只取原 manifest 所列真实文件；不搬 R872 的121 MB载体，不重已有点运算。新一日 carrier 只保本次469件和真实组别。输入数学身份由原 result/run/source/core/manifest、原 certificate、原 configuration 和选择文件指纹组成；纯运输路线不混入数学身份。

源码中的 Source 对所有原选件检查原 manifest/spec、完成证书、source/core/run 三记录和原 configuration。原数学 stage 的完整 tag 保持原 producer，绝不改成 R914。旧 completed 证书中的未直接消费历史叶仍保持原引用，不能把它们假称为本次重新取得或计算。

## 7. CLI、配置与原子阶段

核心：
$$
\texttt{R914\_original\_full\_V1\_involution\_and\_P1\_jets.py}.
$$
入口：
$$
\texttt{--config <expanded-job.json> --out <dir> --budget-minutes 300}.
$$
RESULT 固定为
$$
\texttt{R914-original-full-V1-involution-and-P1-local-jets},
$$
FINAL 固定为
$$
\texttt{p41-original-full-V1-involution-and-P1-jets-certificate.json}.
$$

原 configuration 保存：
真实新 core SHA、python-flint 0.9.0、六组实际 source identities、R912/R802/R805/R853/R872/R883 proof SHA、执行方法 SHA 和固定策略。预算与绝对目录不入数学 tag。新输出统一 $\texttt{R914-iota-*.json.gz}$；每个完整阶段原子写入，complete=true 及 configuration 全同。

关键阶段依次为 source-audit、准确146矩阵、准确全560验证、指定素点矩阵、旧P0 V1表示、新P1 V1展开、准确原点匹配、17个正常组、完整正常 index、原P1参数/t帧。完整 stage manifest 只列真实已成数学阶段，排除自身和 current。预算停止或单位失败保留已成阶段；false FINAL 不作为后续完成断点，不能用其历史 inventory SHA 约束更晚的 current。

成功证书必须同时具有：

- $\texttt{actual\_full146\_exact\_geometric\_iota\_certified=true}$；
- $\texttt{actual\_original\_P1\_normal\_jets\_through\_order272\_computed=true}$；
- $\texttt{actual\_original\_P1\_t\_first\_order\_unit\_certified=true}$。

其中 source-bound 准确矩阵与正常展开 index、原 CM 比对、原 t 帧各有独立真实 bytes/SHA reference。完整 end-point rank8 algebra、Norm determinant values、九范数刚性化、Poincaré period/theta/height 旗标全部为 false。

## 8. 下一实际消费者可直接取得的量

本 scope 实际成功后，R912 的局部八维整阶步骤可以消费真正 P1 的全部正常函数展开；同一原 P/K、global adjugate row 和原 $\Phi$ 的表达式因而能在 P0/P1 两端用同一合法精度规则评价。P1 不再只有三个坐标或一个127维全纯反射。

这不把已取得的273项宣称为未来 Laurent 计算必够。端点实际需要更高阶时，必须沿原 R872 固定单位系统追加尚未算的原 P0 阶，再由本次完整 C 运输；不得重复旧前缀或补造系数。完整 $\operatorname{Nm}(q^*\Phi)\det U$、参考模块与原 $t$ 帧仍由 R912 的后续 rank8 算法分别处理。

