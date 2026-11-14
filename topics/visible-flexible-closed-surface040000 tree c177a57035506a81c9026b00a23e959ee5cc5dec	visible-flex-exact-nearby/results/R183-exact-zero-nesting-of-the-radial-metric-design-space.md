# R183：径向度量设计空间的准确零嵌套

**状态：完整函数嵌套、导数和连续正半径充分域已证明；另名实现的唯一实际局部检查自然退出0。无新完整F、normal、非线性接受态或强闭曲面结论。**

本文件是2026-11-12 21:55执行环境失联后保存的完整证明文本。原本地已登记文本10388B、SHA256 3e29d5bdb48a4a175884cd8ed83ba41bd4e1ca268686cb6594c2ca4e67deb2f3；本次文字恢复不宣称该文件字节相同。原源码、实际报告和二进制身份见第三次失联账本，恢复环境后按身份接续，不能把保存证明当作重新执行。

## 1. 原度量、新支持及准确参数语义

原输入为34真正接受态
`notes/2026-11-12-fd2d-raw-bump-dyadic34-trial-damped-back01-a01-accepted.npz`，
SHA256 `b075e4e5c3dd11b3725eaec47e4d0a5e681d12dd400a4a2e3aff0c3b2f5bd13f`。

其定义含131个径向节点、31个中央参数、16个独立尾参数和7个径向设计参数；物理参数共54维。原度量为
$$
g=ds^2+a(s;\delta)^2du^2,\qquad
a(s;\delta)=a_b(s)+\sum_{j=1}^7\delta_j\psi_j(s).
$$
在保存支持 $L_j<s<R_j$ 上，
$$
\psi_j(s)=1024q_j^5(1-q_j)^5,\qquad
q_j=\frac{s-L_j}{R_j-L_j};
$$
支持外为零。保存的binary64端点和系数本身定义准确有理数；base的准确相位语义按R171/R172。由五阶零点可知每个bump为 $C^4$ 紧支撑函数，且 $0\le\psi_j\le1$。

新设计逐字复制原七个支持，另保存相邻支持端点的binary64平均：
$$
\widehat L_j=\operatorname{fl}((L_j+L_{j+1})/2),\qquad
\widehat R_j=\operatorname{fl}((R_j+R_{j+1})/2),
\quad 1\le j\le6.
$$
新保存端点本身定义准确有理数；不声称它们等于未舍入平均，也不声称准确支持宽度完全相等。每个实际宽度严格正。新支持都位于中央柱与原cut保护邻域之间。

以同一bump公式在新支持上定义 $\widehat\psi_j$，令
$$
a^\sharp(s;\delta,\eta)
=a_b(s)+\sum_{j=1}^7\delta_j\psi_j(s)
+\sum_{j=1}^6\eta_j\widehat\psi_j(s).
\tag{1}
$$
原54参数的顺序不变，六个新系数追加在末端；径向设计维数7增至13，全部物理参数54增至60。原raw P1系数、中央参数、尾参数、网格、固定atlas和参考函数不变。

## 2. 零注入保持完整度量和完整实际场

取 $\eta=0$。由(1)对整个物理域立即有
$$
a^\sharp(s;\delta,0)=a(s;\delta),\qquad
\partial_s^k a^\sharp(s;\delta,0)=\partial_s^k a(s;\delta)
\quad(0\le k\le4)
\tag{2}
$$
于base具有相应片内导数处成立。共同接口上所需jet由新增bump的零迹逐侧相同；这里没有给原base增加未证明的高阶全局正则性。

因此同一物理点的
$$
c=\frac{a_s}{a},\qquad K=-\frac{a_{ss}}a
$$
及原保护区不变。固定atlas $U(s,\xi)$、R139冻结参考和原窗口完全相同；affine lifting使用同一 $a$、同一材料角、中央参数和尾参数，故完整lifting及其存在的jet相同。R153和原R155变换是同一输入上的同一函数复合，所以
$$
(n^\sharp,m^\sharp,l^\sharp)(s,\xi;\delta,0)
=(n,m,l)(s,\xi;\delta)
\tag{3}
$$
在原定义域的每一点成立。

完整角函数、共同角迹、片内物理导数、Gauss–Codazzi缺陷和原cut定义因此相同。原正 $n$ 域及原终端正迹域既未扩大也未缩小。此结论来自函数恒等式，不以四个测试点代替证明；它没有投影、改边界、重求中央曲线或改变尾次数。

由此得到一个包含原近似场的更大度量设计族。零注入不能将原不合格场变成解；之后改变 $\eta$ 是设计新的 $g$，不能声称是最终固定几何的网格、角频率或时间加密。

## 3. 全部旧列与新增六列的完整链式导数

设 $\theta$ 是任一原54参数或raw系数。在共同定义域的可微点，对(3)微分得
$$
\partial_\theta(n^\sharp,m^\sharp,l^\sharp)(s,\xi;\delta,0)
=\partial_\theta(n,m,l)(s,\xi;\delta).
\tag{4}
$$
这要求使用同一独立变量和同一固定atlas；数组增加六列不代表物理坐标移动。

新第 $j$ 列满足
$$
a_{\eta_j}=\widehat\psi_j,\quad
(a_s)_{\eta_j}=\widehat\psi'_j,\quad
(a_{ss})_{\eta_j}=\widehat\psi''_j,
$$
$$
c_{\eta_j}=\frac{\widehat\psi'_j-c\widehat\psi_j}{a},
\qquad
K_{\eta_j}=\frac{-\widehat\psi''_j-K\widehat\psi_j}{a},
\qquad
(1/a)_{\eta_j}=-\frac{\widehat\psi_j}{a^2}.
\tag{5}
$$
直接对上述商函数求导即得(5)。

完整场导数必须把(5)传入lifting、R153/R155变换、实际端点和全部Codazzi RHS，连同角导混合列一起保留。只在Gauss行加入 $-K_{\eta_j}$ 而漏掉半径、lifting或迹变换依赖是不完整的。

参数区间明确为：中央 $[0,31)$，尾 $[31,47)$，原七个径向系数 $[47,54)$，新六列 $[54,60)$。旧参数数值无需移动；全部实际参数数组必须真实扩为60列。旧54列字段消费者或准确证书不可通过伪造标签复用。

## 4. 中央、cut及正则性作用域

每个新bump的支持端点前四阶导数为零，且支持与原中央和cut保护邻域分离。任意有限新增系数都保持这些邻域的原径向定义，包括所需半径jet、原尾定义和原cut参数。

这只证明设计的保护性质，不证明新的GC解、相同空间位置、真实cut两jet匹配、全时reach或握持变化。它们必须由新实际核和真实位置后验另付。

原raw场仍按同一131-node mesh作P1插值。新增光滑bump端点不是新增未知网格节点，不能据此给raw II附加径向正则性；以后若显式细分，另按R163处理准确嵌套与浮点舍入。

## 5. 连续半径正性的有限准确充分域

设已证明 $a_b\ge B>r_*>0$。将所有13个支持端点与物理域端点排序；在任一相邻开区间 $I$，活动支持集合 $A_I$ 固定。令 $\zeta=(\delta,\eta)$。因为所有bump值属于 $[0,1]$，
$$
a^\sharp(s)\ge B+\sum_{j\in A_I}\min(\zeta_j,0).
\tag{6}
$$
若对每个活动集合的所有非空子集 $S\subseteq A_I$ 施加
$$
\sum_{j\in S}\zeta_j\ge r_*-B,
\tag{7}
$$
则整个区间都有 $a^\sharp\ge r_*$。证明是所有子集和的最小值为全部负分量之和；若无负分量则空集给0，而 $B>r_*$ 已单独成立。支持端点由连续性覆盖。

本次具体保存支持给895个去重子集。实现保存整数行系数和准确有理右端语义，并另给浮点计算数组。未来浮点QP容差或采样guard不能冒准确连续证书；最终需准确比较或舍入包含。

本次零注入点由原b075的准确下界 $a>0.78509$ 直接支付，新系数为零不减少它；不依赖一次浮点边界采样判定正性。

## 6. 精确同一函数与有限求积的区别

R165按已声明的物理片边界和bump支持端点分割细积分。即使新增系数为零，新支持端点仍可增加有限Gauss积分分片。对同一个实际函数，不同有限分片规则一般产生不同的近似值和舍入。

因此(3)不等于旧有限残差或旧normal可原样复用。新增六列必须真正装配；若消费者加入新分片，则应计算自己的完整baseline，并如实报告与原有限规则的差异。它们仍对应同一零注入实际场。

最终固定几何加密时，必须冻结所选全部13个径向系数及其余物理参数和时间范围。改变新增系数造成的设计改善不计作该加密。

## 7. 明确源码与已观察的唯一实际局部核

`scripts/fd2d_gc_profile_design_extension.py`：
10540B，SHA256
`0a7f21aa4bd8b42a191096f22ac3234bdb9494d7fce1fbaa5edc67c56a02ae80`。
其新representation为
`ruling_atlas_original_traces_fixed_tail_extended_profile_design_v1`。
原archive仅用于建立原结构，新类明确创建13-bump/60参数、895行半径域和自己的保存恢复定义；没有把新archive伪装旧schema。原source、NPZ、atlas和reference不变。

实际检查为 `scripts/fd2d-profile-design-extension-check.py`，
SHA256 `919fc916f149e9723c5df431cfcc952490f82d38d6f155f30d9c0fca66cbef95`，
输入dyadic35 request，其warm正是b075。
session78794，bb8c88→c4639e；child、wrapper、终端均自然0；
2.746618735秒，RSS134700KiB。

实际结果：
- 节点64/84/118/128，完整值、角导、原54参数列及 $a,a_s,a_{ss},c,K$ 原新差均为0。
- 新六列非零合方向差分：节点64相对差约 $1.875\cdot10^{-10}$，节点84绝对差约 $8.402\cdot10^{-10}$；118/128支持完全分离，新增列为0。
- 完整非零R165 cell64 retained/high新增列JVP相对差约 $1.622\cdot10^{-8}$ / $7.620\cdot10^{-9}$。
- 新断点分片导致原函数有限积分值差约 $1.323\cdot10^{-10}$ / $1.102\cdot10^{-11}$；没有写成相同有限规则。
- 新archive按自己schema真实恢复，完整向量字节保持。

这些是来源绑定的有限实现检查，不是全域导数误差定理，也不是完整场求解。

实际warm：
`notes/2026-11-12-fd2d-profile-design-extension-01-warm.npz`，
135789B，SHA256
`32dd0d4bb82fba78c992db2325cccb6e3f4f995d0e23ea9f6ca4d6d95ee34792`。
原本地7件闭组SHA为
`e5ee10112ebd966524edc294f5b7502ed02897f7eaff5ce4950bcfc35db09ce5`。
其身份包含失联前原证明文本，不能把本次恢复文字冒同一文件SHA。

## 8. 恢复与真正后续消费

恢复源若仍在，先核源/实体身份，不重复已经实际完成的核。只有原实体不可恢复才按保存脚本、dyadic35 request和b075重做；另选输出名保留真实回执：
~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
python scripts/fd2d-run-observed-command.py \
 --receipt notes/R183-replay-process-receipt.json -- \
 python scripts/fd2d-profile-design-extension-check.py \
 --request notes/2026-11-12-fd2d-raw-bump-dyadic35-request.json \
 --out-prefix notes/R183-replay
~~~

这条分支尚无完整F、normal或accepted。若采用，应真正计算60列完整有限目标、约束方向及真实试步。旧34/35 normal不能移用；7维signed窗连续K条件也不能补六个零列冒13维条件。完整强目标继续。
