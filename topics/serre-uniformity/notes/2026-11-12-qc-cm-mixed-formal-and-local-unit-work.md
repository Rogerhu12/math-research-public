# 实际 CM 混合形式值与基点链的整盘恢复

日期：2026-11-12。本文将已经算完的形式值、已验证的链前缀，以及尚待终态的程序分开记录。它们服务于实际全局 QC 截面的搬运，不把局部坐标称为全局高度。

## 1. 同一 R141 框架中的两个真实形式值（已完成）

令 $Y=mB_{-4}$，$C_{12}=P_{-12}-b$，$C_7=P_{-7}-b$，$b=P_{-3}$。
R167 已给 $mC_{12}$ 和 $mC_7$ 在 R141 第一个54点 Abel 族上的实际有效代表；$Y$ 使用第二个族。
原R141/R145两个族的整个126次基除子互不相交，框架不改。

程序 p41_cm_mixed_formal_height47.py 为 $mC$ 重新构造同族的真实负点，并实际求出
$$\operatorname{div}(a_C/v_1^2)=A_1(mC)+A_1(-mC).$$
这里完整199维乘积空间及其包含关系、198阶单位核判据、Frobenius 下降和规范点值全部验证。
第二侧反点函数 $a_B/v_2^2$ 复用 R145 已计算的实际函数。

双逆单位为
$$\delta(mC,Y)=
\frac{(a_C/v_1^2)(A_2(Y))}
{(a_B/v_2^2)(A_1(-mC))}.$$
两个范数都是54个真实移动点的值比的乘积；不动的72点在相同有效代表的差中准确相消。
每一个分母都是47进单位。参数属于 $47R_2$，所以实际截面三阶展开足以保留模 $47^4$ 的全部值。

令 $\mathcal B$ 为 R141 已计算的真实 Hecke 修正矩阵，行对数为 $z_C,z_Y$。R140 的整 Hurwitz 余项界给
$$\lambda_{\mathcal B}(\sigma(mC,Y))
=\frac12\log_{47}\delta(mC,Y)+z_C\mathcal Bz_Y^{\mathsf T}
\pmod{47^4}.$$
这使用同一个代数框架；没有从任意坐标或仅从 Hecke 的切空间矩阵猜测局部高度。

完整结果如下：

| 第一变量 | 第一反点范数 | 第二反点范数 | 半对数 | Hecke 修正 | 实际局部值 |
|---|---:|---:|---:|---:|---:|
| $mC_{12}$ | 207647 | 1868815 | 4049097 | 499234 | 4548331 |
| $mC_7$ | 2491753 | 2387930 | 2491752 | 2065415 | 4557167 |

所有数均模 $47^4=4879681$。两项最后的局部值均在 $47^2R$；双逆对数在 $47^3R$，与次数证明一致。

小证书 p41_cm_mixed_formal_height47_checkpoint.json.gz：
10609字节，SHA256
~~~
99bb809af85c69ea00f18eeabd5a61257952668f45d48acd9f8f440b1fa4cef6
~~~
保存第一反点函数的实际199系数、负点参数及点哈希、完整证明见证的紧凑部分，以及两个范数和修正。可重建的199阶逆大矩阵只保留其 SHA。

这两个值是 $\mathcal P_{mC,mB}$ 中指定范数元素的局部对数；它们不是 $h(C,B)$，也不是 R148 全局规范截面的值。

## 2. 两条 CM 链初始局部因子（完整前缀已验证）

新程序 p41_cm_miller_prepared47.py 从实际199×73理想提取每个剩余盘的完整有效因子，使用 R159 的整 Weierstrass 算法，不对47非单位作除法。
当前26盘的结果：

- CM12 初始有效代表仅在 $P_{-12}$ 盘有 $W=t$；
- CM7 初始有效代表仅在 $P_{-7}$ 盘有 $W=t$；
- 初始主函数 $h=f_b/f_0$ 仅在 $b$ 盘有 $W_h=t$；
- 两个已保存的负点有效除子均避开全部26个盘。

因此在所有盘上逐项验证
$$W_{\rm init}=W_h\,W_{P-b},$$
其中 $P$ 盘的 $W_{P-b}=t$，$b$ 盘为 $t^{-1}$，其余盘为1。

对主函数 $\operatorname{div}F_n=nA_{\rm init}-A_n$，准确式为
$$F_n=V_nW_{\rm init}^{\,n}/W_n.$$
若一次 AddFlip 用截面 $s$，其局部首一因子满足
$$W_s=W_UW_VW_R,$$
所以
$$W_R=W_s/(W_UW_V),\qquad V_R=(V_UV_VU_s(0))^{-1}.$$
加法的第二输入是 $+C$ 或 $-C$ 时，必须分别使用 $W_{\rm init}$ 或 $W_{-C}$，不能沿用原 $B$ 链中两者均为1的简写。

已完成的真实前缀为：

| 链 | 位数/步数 | 最大截面局部阶 | 证书 SHA256 |
|---|---|---:|---|
| CM12 | 30 / 45 | 3 | 198968a097e32df60b00f2f0b3e762f2c49040bdbd03f043283b134800433bfd |
| CM7 | 15 / 22 | 2 | b99baea6b02f158ddc5abe0f17597435837f48d455cef7d7aeb577c7979f11af |

每个前缀末尾都从当前完整有效除子理想独立取最小阶生成元，核对其 Weierstrass 因子与递推所得完全一致。这里的“独立”指没有将递推的因子当作理想输入；没有重复群运算。

## 3. 真正 based 函数与未运行终态的入口

p41_cm_endpoint_transport47.py 是终态程序，须在相应链完成304位后运行。
它由完整理想求函数
$$g_{\rm tr}=(s_{\rm new}/f_0^2)/(s_{\rm old}/f_0^2)/(v_1/f_0),$$
并验证
$$\operatorname{div}g_{\rm tr}=A_{\rm formal}-A_{\rm old}.$$
对 CM7，它在819个忠实评价点上执行实际核与单位同构，再把截面系数转回原199基。程序没有给尚未评价的函数范数赋值。

由于原链起始代表为 $A_{\rm init}=P-b+\operatorname{div}h$，最终真正函数是
$$\boxed{f_C=\frac{F_{\rm chain}}{g_{\rm tr}h^m},\qquad
\operatorname{div}f_C=m(P-b)-A_{\rm formal}.}$$

对每个盘，程序将完整记录 $f_C$ 的真实阶和首单位：
$P$ 盘为 $+m$，$b$ 盘为 $-m$；其余所列盘阶为零，才可把首单位称为普通函数值。
R148 使用 $j-j(P)$ 参数，若要使用这些任意固定整参数下的首单位，仍须实际换算参数的一阶单位及相同线丛生成元。本文不把这项转换省略成常数。

链完成后可由全部325维主截面系数直接重放任意形式第二变量上的范数及54个三阶展开，无需再跑一次大整数 Jacobian 乘法。
结合第1节即可得到指定非形式第一变量的局部值；仍须另完成 R148 全局规范截面的实际纤维运输。

p41_cm_local_connection47.py 已写成该终态重放入口，但本笔记写成时两条304位链仍在运行，故不声称此入口已产生最终值。它明确先扣除终点函数，再扣除 $m\log h(A_2(Y))$，并用
$$m\lambda(e(P-b,A_2(Y)))=\lambda(\sigma(mC,Y))+\log f_C(A_2(Y))$$
求值；54个导数仍只认证到模 $47^3$。这个入口没有执行另一条 Jacobian 长乘。

## 4. 命令与现行文件

~~~
python -B scripts/p41_cm_mixed_formal_height47.py --script-dir scripts

python -B scripts/p41_cm_miller_prepared47.py --script-dir scripts --discriminant 12 --miller scripts/data/p41_cm12_slp47_30_fixed.json.gz --output /tmp/p41_cm12_prepared.json.gz
python -B scripts/p41_cm_miller_prepared47.py --script-dir scripts --discriminant 7 --miller scripts/data/p41_cm7_slp47_15_fixed.json.gz --output /tmp/p41_cm7_prepared.json.gz

# 以下命令须待相应实际304位链完成；当前不宣称已运行终态：
python -B scripts/p41_cm_endpoint_transport47.py --script-dir scripts --discriminant 12 --miller /tmp/p41_cm12_slp47_rolling.json.gz
python -B scripts/p41_cm_endpoint_transport47.py --script-dir scripts --discriminant 7 --miller /tmp/p41_cm7_slp47_rolling.json.gz
python -B scripts/p41_cm_local_connection47.py --script-dir scripts --discriminant 12 --miller /tmp/p41_cm12_slp47_rolling.json.gz
python -B scripts/p41_cm_local_connection47.py --script-dir scripts --discriminant 7 --miller /tmp/p41_cm7_slp47_rolling.json.gz
~~~

输入的 R141、R145、R160、R167 原始恢复数据与各自证书哈希绑定；重建方式仍见各已发布恢复笔记。

