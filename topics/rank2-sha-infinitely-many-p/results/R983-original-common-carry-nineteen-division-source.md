# R983 — 保原共同 carry 的十九倍 degree390 来源与完整五伴随

日期：2026-11-27。**已证明：下面的真实六 sigma 来源属于原完整 degree390 空间，保 R968 同一 C/F 及四输出；全部十九倍除法、整框架和四方向 CM 五伴随转移成立。** 对 R976 两个新质量零块的实际投影由同次完整消费者读取，结构本身不预设投影非零。

## 1. 原六输入上的完整新轴

保持 $E_1:y^2=x^3+1$、$dz=dx/(2y)$、$\omega^2+\omega+1=0$、
$\delta=1+2\omega$、$\rho=-\nu_\sigma^{\otimes6}/84$，原输入顺序
为 $(\xi_1,\xi_2,\xi_3,x_0,c,d_0)$。置
$$
\gamma=3+\omega=(5+\delta)/2,\qquad N\gamma=7,
$$
$$
\boxed{a_{19}=(2+\omega,2+\omega,1,\omega^2,19,\delta\gamma),
\qquad Y_{19}=a_{19}\xi.}
\tag{1}
$$
六个范数依序为 $3,3,1,1,361,21$，和为390。前四项与 R977 完全相同，
后两项不被 R968 的原
$$
H_0=(1,0,-1,1,0,0),\qquad H_1=(-1,2,\omega,1+\omega,0,0)
$$
读取，所以其完整内积仍为
$$
\boxed{a_{19}\bar H_0^t=a_{19}\bar H_1^t=0.}
\tag{2}
$$
固定原 $C=H_0/\delta$、$F=-\omega H_1/\delta$。没有换共同平面。
所有六个系数模2非零，六个原 odd 半特征的乘积为标准 even 半特征；
范数和390消去 Gaussian 交叉项，共同六次旋转给 principal 型。

原首边际的准确归一为
$$
\boxed{\mathcal F_{19}=\frac{28}{19\omega\delta\gamma}(a_{19})_*\rho.}
\tag{3}
$$
它来自实际推前，未由目标特征线反选一个函数。

## 2. 原 norm7、norm21 与完整十九倍除法

写 $X=x^3$。原 norm7 division 身份是
$$
\sigma(\gamma z)=\gamma\sigma(z)^7R(X),\qquad
R=X+\frac{-2+6\delta}{7}.
\tag{4}
$$
它是 R958/R961 同一 CM 群律与原 sigma 相位的完整除法式。
绝对常数也可在原全除子固定后由首项核定：
$\gamma^6=-143+180\delta$，原 $\sigma=z+z^7/210+\cdots$、
$X=z^{-6}-3/7+\cdots$ 给 $R-X=(\gamma^6+83)/210$，恰为 (4)。
这里先用完整 division 除子确定一次式，不凭一个截断展开识别任意函数。

对 (4) 取二次对数导数，得到
$$
x(\gamma z)=\frac{xA(X)}{\gamma^2R(X)^2},
$$
$$
\begin{aligned}
A&=7R^2-6(7X+4)RR'-36X(X+1)(RR''-R'^2)\\
 &=X^2+(20-24\delta)X-8-24\delta.
\end{aligned}
\tag{5}
$$
这使用 $(X')^2=36xX(X+1)$ 和 $X''=6x(7X+4)$。
结合原 $\sigma(\delta z)=\delta x(z)\sigma(z)^3$，完整组合给
$$
\boxed{\sigma(\delta\gamma z)=\delta\gamma\,xA(X)R(X)\sigma(z)^{21}.}
\tag{6}
$$
因此 norm21 的所有核点、重数、常数与原微分一并保留。

令 $\psi_n$ 为 $\mathbf Z[x,y]/(y^2-x^3-1)$ 中的原全部 division 序列：
$$
\psi_0=0,\quad\psi_1=1,\quad\psi_2=2y,\quad
\psi_3=3x(X+4),\quad\psi_4=4y(X^2+20X-8),
$$
$$
\psi_{2m+1}=\psi_{m+2}\psi_m^3-\psi_{m-1}\psi_{m+1}^3,
$$
$$
\psi_{2m}=\frac{\psi_m}{2y}
 (\psi_{m+2}\psi_{m-1}^2-\psi_{m-2}\psi_{m+1}^2).
\tag{7}
$$
偶式的除法在此原曲线整环中准确整除。对奇数19，原 sigma 规范给
$$
\sigma(19z)=\psi_{19}\sigma(z)^{361},\qquad
\psi_{19}=\psi_{11}\psi_9^3-\psi_8\psi_{10}^3.
\tag{8}
$$
全部奇19-kernel及其重数是 (7)–(8) 的完整 division 除子。
$\mu_6$ 权及 $\deg_x\psi_{19}=180$ 给
$$
\psi_{19}\in\mathbf Z[X],\qquad\deg_X\psi_{19}=60,
\qquad[X^{60}]\psi_{19}=19.
\tag{9}
$$
式 (7)–(9) 完整指定这61个系数，不需要保存生成系数表。

原前四 sigma 的乘积为 $-3\omega x^2\sigma^8$。
乘 $-1/84$、再用 (3)、(6)、(8)，得到完整函数身份
$$
\boxed{F_{19}(z)=\frac{x^2\sigma^8\sigma(19z)\sigma(\delta\gamma z)}
 {19\delta\gamma}
 =\sigma^{390}\frac{X\psi_{19}(X)A(X)R(X)}{19}.}
\tag{10}
$$
右边多项式次数 $1+60+2+1=64$、首系数1，故在原完整
$V_{390}=\sigma^{390}K[X]_{\le65}$ 中，质量第65列为零、第64列为一。
原点阶准确六，首项一。没有由 degree390 或六个 odd 数量猜出投影。

## 3. 完整整框架、半特征与两个逆

从 (1) 开始，按零起始指标 $4,5,0,1,2$ 删除，最后留指标3。
在每个实际剩余集 $I$ 中置 $N_I=\sum_{j\in I}N(a_j)$，并取
$$
r_i=N_Ie_i-\bar a_i a_{19}|_I.
\tag{11}
$$
原完整范数链为
$$
390,29,8,5,2,1.
$$
各行逐对正交，$N(r_i)=N_I(N_I-N(a_i))$。首行与五行组成
$L_{19}\in M_6(\mathbf Z[\omega])$，于是
$$
\boxed{L_{19}\bar L_{19}^{,t}
 =\operatorname{diag}(390,11310,232,40,10,2).}
\tag{12}
$$
模2的非零系数个数逐行为 $6,6,4,4,2,2$；因此每个输出都是完整 even
半特征的原 theta 空间，全部 Gaussian 交叉项为零。两个准确逆由
$$
(L_{19}^{-1})_{ji}=\frac{\overline{(L_{19})_{ij}}}{N_i}
\quad (N_i=390,11310,232,40,10,2)
\tag{13}
$$
逐项返回。特别
$$
\boxed{N(\det L_{19})=(390\cdot29\cdot8\cdot5\cdot2)^2.}
\tag{14}
$$
其素因子只有 $2,3,5,13,29$，与 $7\cdot19$ 互素。
虽然 (1) 某些单个系数可被指定 CM 素元整除，整个矩阵在每种
7/19-kernel 上仍可逆；所需条件是 (14)，并非每个单轴系数各自可逆。

完整联合来源为
$$
\frac{28}{19\omega\delta\gamma}(L_{19})_*\rho
 \in\mathcal S_{390}\otimes\mathcal S_{11310}\otimes
 \mathcal S_{232}\otimes\mathcal S_{40}\otimes
 \mathcal S_{10}\otimes\mathcal S_2.
\tag{15}
$$
第一边际恰是 (10)，不由该边际反推联合来源存在。

## 4. 原 CM 五伴随与新目标的实际读取

R961 已支付四个方向 $\gamma_7,\bar\gamma_7,\gamma_{19},\bar\gamma_{19}$
的奇 sigma 绝对身份 $N_\beta\sigma=\sigma$。
由 (14)，完整六重 CM 核在 $L_{19}$ 下双射；重排全部有限纤维给
$$
N_{\beta,Y_{19}}\prod_{i=1}^5N_{\beta,Z_i}
 \left(\frac{28}{19\omega\delta\gamma}(L_{19})_*\rho\right)
=\frac{28}{19\omega\delta\gamma}(L_{19})_*\rho.
\tag{16}
$$
每个 $1/\beta$、奇半特征、canonical division lift 和有限中心都保留。
第一 principal 平均可按 R980 用五伴随同时旋转实现；其后第一轴
任意完整 CM 多项式均可转到相反方向的五伴随。

对 R976 固定的全66列秩一块 $(2,3),(3,5),(5,3)$，按该篇的首阶六
规范记来源为 $Z,\Psi_{3,5},\Psi_{5,3}$。后两条的全部有限算术身份
与秩下界由 R981 给出，不能只用这里两好位特征指定曲线。
实际消费者须返回全部66行
$$
\Pi_{2,3}F_{19}=\alpha_{23}Z,\qquad
\Pi_{3,5}F_{19}=\alpha_{35}\Psi_{3,5},\qquad
\Pi_{5,3}F_{19}=\alpha_{53}\Psi_{5,3}.
\tag{17}
$$
结构证明没有指定任何 $\alpha$ 非零。
若某个实际 $\alpha_b\ne0$，完整第一轴秩一投影及 (16) 才给
$$
\Pi_{b,Y_{19}}\frac{28}{19\omega\delta\gamma}(L_{19})_*\rho
 =\Psi_b\otimes\Lambda_b,\qquad\Lambda_b(0)=\alpha_b.
\tag{18}
$$
对好普通 $p$，在所有固定分母和 $N(\alpha_b)$ 的有限坏集之外，原整 Amice 格及首阶六
提取证明 $\Lambda_b$ 是完整五变量整卷积单位。不预先把这个有限集说成
$p\le211$，也不把三个伴随来源认作相同。

## 5. 同一 C/F 与所有旧 mixed 条件

由 (2)，原四输出投影 $\pi=I-\bar C^t C-(3/7)\bar F^t F$ 满足
$a_{19}\pi=a_{19}$。所以 R968 的同一个十二次 carry 给整个边际
$$
\int_{Y_{19}\,\mathrm{unit}}\langle Y_{19}\rangle^{(p-1)u}
\mathfrak q_{n,p}^{\rm new}\,d\rho
=\upsilon_p^n\int_{Y_{19}\,\mathrm{unit}}
 \langle Y_{19}\rangle^{(p-1)u}\,d\rho.
\tag{19}
$$
第一轴的完整 CM trace/pull 及每个真实 finite 中心也保持 $C,F$，
故对 (18) 的已投影来源仍成立。

每条旧实际观察 $r$ 先写成 $rL_{19}^{-1}$ 并完整乘回。
在五伴随的分支 $\beta=\gamma_7^j\gamma_{19}^k$ 与同时角旋转
$\eta\in\mu_6$ 中，连续观察为
$$
(rL_{19}^{-1})_0Y_{19}
 +\frac{\eta}{\bar\beta}\sum_{i=1}^5(rL_{19}^{-1})_iZ_i,
\tag{20}
$$
并加上该分支全部实际 torsion 中心。旧 $S,T,W^\pm,Z,F_{10},F_{11}$ 的
单位域、深管、logarithm 和观察次序均读取整个 (20)。
共同 carry 保持不意味着这些条件已变为独立伴随测试；完整补域仍须消费。

## 执行入口与当前范围

新 `scripts/check-original-degree390-common-carry-nineteen-source.py` 将消费同次原
66列 CM 上下文，从 (4)–(10) 现造全部来源、从 (11)–(14) 现造完整
框架，读取 (17) 的实际三标量及全部81个余块。它不读取保存的系数、
矩阵或前次运行结果。源码和实际回执由后继执行节记录。

本篇已经支付的是新真实来源、全除法、整五伴随及同一共同 carry；
目标投影和跨 $p$ 中央非零各自保留准确的实际门。


### 同次中央 v8 的固定源码

十九来源 helper SHA-256 为 `1561d8582663191633db56d1cf02c19d69d5d3b33271dd19b700f3c2060c7ae3`，四新来源角/十低行 helper 为 `4bfa7783e5fc307a1a5a332a25a95340060bd83a58c4e5a04ff5c52f2c0ddfaf`。主入口/request/workflow 升为 v8；17份依赖 pins、20份完整 source manifest、18份 Python AST，保 v7 全部旧门。数学只在本题公开 Actions 中执行，结构登记时尚未预记结果；实际成功回执及其完整消费如下。

## 6. 同次原66列实际非零、完整单位伴随与物理尺度

中央 v8 source 为 `c3fc3c60605f4455fc57177367c89e56a9763f6a`，
[run45892525657](https://github.com/Rogerhu12/math-research-public/actions/runs/45892525657)，
job `140158402506`，2026-11-26 20:38:41–20:46:00 UTC，实际 `success`。
所有旧消费者均保留，本 helper 用时9.892560351秒；全部20源 manifest、完整日志和 stdout 的摘要见 R982 §7。

同一原全66矩阵、完整十九倍 division 与全部81个块给出
$$
\boxed{
\begin{aligned}
\alpha_{23}&=\frac{75-50\delta}{57}=\frac{25(3-2\delta)}{57},\\
\alpha_{35}&=\frac{210+350\delta}{57}=\frac{70(3+5\delta)}{57},\\
\alpha_{53}&=\frac{2505-1670\delta}{57}=\frac{835(3-2\delta)}{57}.
\end{aligned}}
\tag{21}
$$
每一个等式都返回全部66坐标，目标投影秩均准确为一；没有只比首项。
$F_{19}$ 本身的完整多项式次数64、首项一、质量零和最小整数分母
$$
D_{F_{19}}=133=7\cdot19
\tag{22}
$$
均实际返回。三个目标的最小分母依序是175、245、5845。
全部81个幂等元和为恒等、全部81个实际分量和为原 $F_{19}$；完整非 $\mu_6$ 余分量实际非零，不能删去。

由 $N(a+b\delta)=a^2+3b^2$，(21) 的三个范数准确为
$$
\boxed{
N\alpha_{23}=\frac{5^4\cdot7}{3\cdot19^2},\qquad
N\alpha_{35}=\frac{2^4\cdot5^2\cdot7^3}{3\cdot19^2},\qquad
N\alpha_{53}=\frac{5^2\cdot7\cdot167^2}{3\cdot19^2}.}
\tag{23}
$$
所以三者均非零，且对每个好普通 $p>211$，三者在原 CM 系数环的每个
$p$-进分支上都是单位。新增分母245和5845只涉及5、7、167；原框架
(14)只涉及2、3、5、13、29，四 CM 核只另涉及7、19，原有限投影分母
及 ray 费用仍已由 R959/R981 支付。因此本篇原先暂留的固定坏集现在已经由
实际(21)–(23)付清：在原好普通 $p>211$ 的范围内，三个完整伴随均为单位。

具体地，施第一轴完整投影得到真实全联合身份
$$
\boxed{\Pi_{b,Y_{19}}\frac{28}{19\omega\delta\gamma}(L_{19})_*\rho
=\Phi_{b,1}\otimes\Lambda_b,\qquad
\Lambda_b(0)=\alpha_b\in\mathcal O_p^\times,}
\tag{24}
$$
其中 $b$ 在本式只是三个已固定目标的索引，实际曲线常数仍分别为
$B=65,54925,8125$。这三份 $\Lambda_b$ 不被相互认同。
原全来源及全部有限算子在同一普通 Amice 格中整；每个归一目标从
$z^6$ 起且首项一。读取第一 Amice 变量的第六项，除去原单位周期的六次幂，
便得 $\Lambda_b$ 的全部五变量系数在 $\mathcal O_p$ 中。
再由(23)的常数单位，完整 Amice 级数可逆，故 $\Lambda_b$ 是完整五变量
**整卷积单位**，不是仅有一个非零质量的边际。

对两条新曲线，R981 的物理来源始终是
$$
\Phi_{B,B}(z)=B^{-1}\Phi_{B,1}(\theta_Bz),\qquad
\widehat\Phi_{B,B}=D_B\Phi_{B,B},\qquad\theta_B^6=B,
$$
$$
(B,D_B)=(54925,245),(8125,5845).
\tag{25}
$$
在原共同模型17和已经固定的相容微分/周期下，(24)的第一轴与算术来源
比较保留固定比例
$$
\boxed{\frac{B}{17D_B}.}
\tag{26}
$$
这两个比例也都是 $p>211$ 的单位；三处 $+i$、5处 odd 向量、双13的
全部有限角色、原 CM/Tate 张量和同权平方常数均沿 R981 原规范保留。
(26)不被吸收到一个未标明的重新选取周期中。

因此两条新固定 rank 至少二曲线的真实中央零，可以在(24)的各自完整
联合来源上配任意独立伴随测试使用。若要回到原 $S,T,W^\pm,Z$ 的 mixed
域，仍须用(20)的全部真实行与有限中心；逆卷积也会平移那些测试。
原共同 C/F carry 继续由第5节保持，不能因此删去混合补域。
惰性中央仍使用 R981 的原完整 Newton 和 signed 通常群比较；这里的普通
Amice 单位证明没有冒称惰性五变量单位测度。

必要的新增摘要为：

- 原完整 $\psi_{19}(X)$：`24330aebbef6d267e8c583dab7cb25be8c8cea97e5fc88fa0c5c50651e55e53b`。
- 原 norm7 $R$：`f099cfa9ba9975bc8fe8f4d675f7dfe1546d0858cb82a37f23e232e2768c6fa2`；$A$：`8c12c62e7aecb2ab4cc6faecd6cbfb2deb1435dd7ce1a26afd0a5474ba37a95d`。
- 全66来源：`93983110115b07d9ed680fa3f5f26b41e40dc826eecc7b02a471a73d96e251d8`。
- 整框架：`9499f61d97045c610a3d66cbaf6d05dac82d70e14bb5ca5a31220ad8fd657500`；整逆：`c7363d220cc3d32cad998138aec60cdec37d559cf5537112520931820ab3d3e3`。
- 实际 $N(\det L_{19})=818663040000$，全半特征 odd 个数为 $(6,6,4,4,2,2)$，Gram 和两向逆全部返回。
- 完整非 $\mu_6$ 余分量：`1417549ad40dd7356806ea8bab24e9a414e3548604a4ca4c2ff27d6ec64fe00a`。

实际返回还包括原 $S,T,W^+,W^-,Z,\mathcal F_{10},F_{11},F_{19},H_0,H_1$
的全逆坐标和逐行乘回，尤其后两行第一坐标准确为零。这里完成的是两条新算术
来源的真实完整伴随；主目标仍须消费这些来源迫出无穷多个素数上的中央非零。
