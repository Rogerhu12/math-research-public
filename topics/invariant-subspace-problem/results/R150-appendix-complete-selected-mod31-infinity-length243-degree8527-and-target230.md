# R150：同一原子式完整模31无穷远长度243、次数8527及条件目标成本230

日期：2026-11-15 UTC。Astra-ISP-789f；AI 辅助，GPT-6 Astra Pro。

同一原 $I,J$ 的自然 Schur 系列现已在新的真实运行中完成全部36个正 Smith 指数，精确总和为243。原十六阶的51份完整数组逐系数身份均已复核。保持总权8770，因此同一子式模31的次数准确为8527，特征零次数至少8527；配已付 $K_{89}$，条件目标分支的来源成本从8442降到230。全部原来源转移的统一条件成本仍为8654。

本稿不再留有限域长度的未定块。特征零完整长度、最高系数的31单位性与原目标成员性仍是后继的独立问题。

## 1. 原数学对象与真实重做

保持[原自然八阶 Schur 证明](R150-appendix-selected-natural-schur-eight-jets-and-mod31-order184.md)中的
$$
A^h(u):\mathbb F_{31}[[u]]^{6188}\longrightarrow
\mathbb F_{31}[[u]]^{4367},\qquad
B(u)=A^h(u)_{I,J},\quad |I|=|J|=4354.
$$
原自然参数为 $u=1/s$；方阵常数秩为4318，余块为36维。全部来源和输出坐标、原十七式、原整数内容归一均保持。

旧run43679903558的32阶数学结果曾出现在日志中，但发布摘要越过100000字节上限，作业结束，临时数组丢失。本次没有以旧日志充当新的完成证书，而按[最小恢复计划](../notes/2026-11-15-r150-unpublished-natural32-minimal-recovery-789f.md)实际重建并重做。

[最小重建源码](../notes/2026-11-15-r150-selected-natural-u-minimal-rebuild-789f.py)从明确固定的历史Git对象读原native、point、原选集合、kernel36及3333/985来源DAG，只建立必要的原字典和first缓存。原数学runner、native与两头文件字节不变；重建文件使用真实新输入身份，不冒称原gzip容器字节已恢复。

新的Schur绑定是
~~~
43124d7d621b24353e3686cb1db8932ee6259822f22c1dbb1f8e0cd1d7b54600
~~~
新的first绑定是
~~~
c11dd73f0b8f469a8c1abee84de0b8ff7a38906a992376a16129a44fcad8607b
~~~

## 2. 完整前十六阶系数一致，而非只比较秩

[已发表十六阶记录](R150-appendix-selected-natural-schur-sixteen-jets-and-mod31-order237.md)保原 $k=0,\ldots,16$ 三类数组的全部SHA：

- $6188\times36$ 原来源 $X_k$；
- $36\times36$ 同选 Schur 系数 $S_k$；
- $4367\times36$ 全原输出残量 $E_k$。

每份二进制文件前24字节记录magic、域、阶数和尺寸，随后64字节是输入绑定，再后是完整有限域数组。本次只在比较用字节串中把新64字节绑定归一为旧绑定，全部51份文件的完整大小和SHA都与已发表值一致。没有改变任何数学系数，也没有改写实际新文件。

本次实际回执同时给
~~~
all51PaidPrefixFilesCoefficientIdentitiesVerified=true
allSeventeenPaidSmallSchurCoefficientsVerified=true
~~~
并保原33条第一校正全部4367输出乘回、全部4354选输出分解、36自由坐标和同一来源支撑。

由原单位块图递推，
$$
X_0=K_0,\qquad
X_k=-W\sum_{i=1}^{\min(k,10)}A_iX_{k-i},
$$
所得 $S(u)$ 是同一 $B(u)$ 的真实形式Schur余块，而且
$$
\det B(u)=\varepsilon(u)\det S(u),\qquad
\varepsilon(0)\ne0.
\tag{2.1}
$$
这次实际生成至32阶，在21阶处已经消去最后一个正指数方向。

## 3. 完整正 Smith 指数

全部正指数的重数为：

| 指数 | 重数 | 对总长度的贡献 |
| ---: | ---: | ---: |
| 1 | 3 | 3 |
| 2 | 9 | 18 |
| 3 | 3 | 9 |
| 4 | 3 | 12 |
| 5 | 3 | 15 |
| 6 | 1 | 6 |
| 7 | 2 | 14 |
| 8 | 1 | 8 |
| 11 | 3 | 33 |
| 12 | 2 | 24 |
| 13 | 1 | 13 |
| 14 | 1 | 14 |
| 17 | 1 | 17 |
| 18 | 2 | 36 |
| 21 | 1 | 21 |
| **总计** | **36** | **243** |

此外有4318个零指数。16阶之后新增的最后四个正指数准确为
$17,18,18,21$，贡献74；与此前32个指数之和169相加得到243。

每层小单位Schur消元都验证实际单位块逆和余块系数，最后在21阶取得一维单位块，剩余维数为零。因此无需把截断零块猜为形式零块：所有指数都已实际确定，后面的未知高阶项不能改变已提取的单位主项。于是
$$
\boxed{v_u\det\overline B(u)=243.}
\tag{3.1}
$$
回执明确为 completeSelectedInfinitySmithLengthComputed=true、
unresolvedCount=0。

同一Smith定理还给全部同选低一阶子式生成的理想
$$
I_{4353}(\overline B)=(u^{243-21})=(u^{222}).
\tag{3.2}
$$
所以在有限域中，这批cofactor的公共阶准确为222，至少一个达到该阶；同一逆矩阵的最大极点阶准确为21。这两项均限于同一有限域方阵，未升为特征零下界。

## 4. 同一子式的精确有限域次数与特征零区间

令 $D(s)$ 是前稿同一个选定原子式，保持31单位的整数内容归一。自然齐次化的总权为
$$
H=8770,\qquad D_h(u)=u^H D(1/u).
\tag{4.1}
$$
原 $D$ 定义在 $\mathbb Z_{(31)}[s]$ 上。由 (3.1)，
$$
\boxed{\deg\overline D=8770-243=8527.}
\tag{4.2}
$$
这同时证明 $\overline D\ne0$。模31次数不能超过原特征零次数，故
$$
\deg_{\mathbb Q}D\ge8527.
\tag{4.3}
$$

[原无穷远第三页与29精确曲线](R150-appendix-infinity-third-connection-one-dimensional-bound-order43-and-cost8663.md)
已给特征零同选消失阶至少72，即 $\deg_{\mathbb Q}D\le8698$。
因此现在严格得到
$$
\boxed{8527\le\deg_{\mathbb Q}D\le8698,}
\qquad
\boxed{72\le v_uD_h\le243.}
\tag{4.4}
$$

由于 $\overline D$ 的8527次系数非零，最高系数的31单位性可以准确改写为
$$
\boxed{
\operatorname{lc}(D)\in\mathbb Z_{(31)}^\times
\ \Longleftrightarrow\
\deg_{\mathbb Q}D=8527
\ \Longleftrightarrow\
v_uD_h=243.}
\tag{4.5}
$$
若特征零次数更高，则那些高于8527次的系数都模31为零，其中真正最高的系数不是31单位。本稿尚未排除这些系数在特征零非零。完整有限域长度的确定，因而把原首项单位缺口定位为 (4.5) 的精确次数问题，并未自动解决它。

## 5. K89 下的新 q 区间与目标成本230

[有限零点三阶证明](R150-appendix-zero-twenty-two-third-left-jets-factor89-and-cost8654.md)
已给公共因子 $K_{89}$，次数89，最高系数 $5^6$ 为31单位。令
$$
d_*=D/K_{89},\qquad q=\deg d_*.
$$
由 (4.4)，
$$
\boxed{8438=8527-89\le q\le8698-89=8609.}
\tag{5.1}
$$
此前仅由仿射gcd次数315所得的下界226，现在可替换为8438。

保持同一原来源权，$\max a_\ell=55$、$\max(a_\ell-10)=45$。
特征零的原来源换列阶至少71、cofactor阶至少67。原来源转移多项式仍为
$$
P_\ell=\operatorname{adj}(A_{I,J})(A_\ell)_I/K_{89},
\qquad A_JP_\ell=d_*A_\ell.
$$

明确假定原目标 $b_\nu=h_0t_\nu$ 已属于
$\operatorname{im}_{\mathbb Q[s]}A$，且其自然权 $\tau_\nu\le64$。
成员性使
$$
T_\nu=\operatorname{adj}(A_{I,J})(b_\nu)_I/K_{89}
$$
为多项式，仍有
$$
\deg(T_\nu)_j\le H-a_j+\tau_\nu-67-89.
\tag{5.2}
$$
沿前稿同一个非基除法和来源转移构造，三类成本变为
$$
\begin{aligned}
q-1+45&\le8653,\\
8770+55-71-89-11&=8654,\\
8770+64-67-89-10-8438&=230.
\end{aligned}
\tag{5.3}
$$
所以目标分支已有230界，统一原来源成本仍由转移分支控制：
$$
\boxed{
h_0t_\nu\in\operatorname{im}_{\mathbb Q[s]}A
\Longrightarrow
\exists y_\nu:\ Ay_\nu=h_0t_\nu,\quad
\operatorname{cost}(y_\nu)\le8654.}
\tag{5.4}
$$
(5.3) 没有用有限域cofactor的222代替特征零67，也没有假定 (4.5) 已成。原目标成员性和最终特征零首项单位继续分别验证。

## 6. 新的实际运行

实际 run **43702348535**，step **selected-natural-u-minimal-rebuild32**，
执行源码提交 **ddcde7bb70852f5b065b21345c5d7147de58184f**。
共享数学60秒、内存512MiB、编译上限30秒；实际数学用时
**10.855262523000079 秒**，其中 native **9.937256051 秒**，
外层墙钟 **16.904246578000084 秒**，退出码0。

原完整临时重建回执14906字节，SHA256：
~~~
81e0f05da228f523369513ced5eb0a085f7364ef53a2a6219e90ed94502a900e
~~~
原数学引擎临时回执65497字节，SHA256：
~~~
298105020cd19f41f4869799e81e2f63125ed7d5d0477b3fa547afa95ab103d3
~~~
最小重建源码SHA256：
~~~
bb4a217827ff7a8ac8faf9c0f1b2c5255e302c3bcc66f644cd31a8f8f50312c6
~~~

[本次已推执行记录](../notes/r150-infinity-remote-session-789f/43702348535-selected-natural-u-minimal-rebuild32.json)
保实际全部输入身份、51份前缀比较、全部Smith层、完整原乘回标志和新绑定。
新数组仍只存在当前作业临时目录；没有重新上传Git、Release或大工件。后继直接使用这个真实检查点。
