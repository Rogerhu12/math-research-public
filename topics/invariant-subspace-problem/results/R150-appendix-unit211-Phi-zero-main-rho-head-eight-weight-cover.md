# Phi=0 主 rho 二次头零支：完整原投影将不同主权参数压到八个

数据保存说明（2026-11-28）：可重算载荷已按根规矩8/15从main移除，相关旧链接只定位既有历史；当前保留生成源、参数定义、run与SHA，原数学及执行身份不变。


日期：2026-11-28（Asia/Taipei）  
会话：Astra-ISP-8542378f-20261127

## 1. 范围与结论

接 [主头零 C71,29](R150-appendix-unit211-Phi-zero-main-head-zero-mean-T-unit-six-C71-29.md) 的同一个原 unit211、LS、$\Phi=0$、物理 $D\ne0$ 图。记
$$
d=b-c,\qquad \rho=-d,\qquad v=d^2,
$$
$$
u=1+v,\qquad Q=1-v,\qquad \ell=1+2v.
$$
本稿证明该图中不同的 $v$，以及由它唯一决定的 $(u,Q,\ell)$，合计至多八个。具体保留整条首项零纤维
$$
H_7(v)=48v^7+36v^6-12v^5+15v^4+42v^3-4v^2+2v+1=0
$$
的至多七个根；其补图中不同 $v$ 至多一个。

这不是全部 $(\lambda,T,z)$ 原值点数的界。$d$ 的两个符号以及原 B/C 有序标签仍按原交换处理，不能把它们额外计为同一个有序权点。本稿没有排空八个权参数对应的原值纤维，也没有把模线性因子直接认作已恢复的有理因子。

整个另一个特殊有序权图 $\ell=3/2,\ u=(\rho+3)/2,\ Q=1-\rho^2$ 已由 [原 P6 整图返回](R150-appendix-unit211-Phi-zero-exceptional-weight-chart-complete-original-exclusion.md) 关闭；本稿处理的是上述主图，不借用该特殊图的结论来删除本图权参数。

## 2. 已付原输入与完整首项零分解

只读取以下三个已保存的精确原必要式：

- [P6](R150-appendix-unit211-Phi-zero-first-quadratic-head-actual-D-sixth-degree-necessary-equation.md)：一般第一二次头非零图上的 $P_6(u,Q,\lambda)=0$。
- [P9](R150-appendix-unit211-Phi-zero-first-head-complete-original-F6-row-and-D-nine-necessary-equation.md)：同一图上的 $P_9(u,Q,\lambda)=0$。
- 主图上不需要该第一头非零的 $C_{71,29}(v,\lambda)=0$。

P6/P9 来源的原单位目标、F6 递推及 C71 的旧六行 Cramer 计算均没有重做。P9 由已保存清单及五个带 SHA 的小片段完整重建；程序实际核验所有原载荷及完整多项式摘要。

第一二次头记为 $H_1$。既有全权四次 $g=-12H_1$ 在本图准确满足
$$
4g(1+v,1-v)=H_7(v).
$$
这项完整多项式恒等式由新输入实际乘回。因此只在 $H_7(v)\ne0$ 的补图使用 P6/P9；$H_7=0$ 的全部复根在结论中单独保留，没有把 $H_7$ 当作全局原单位。

原权关系还给出
$$
T_0=-1-3v,\qquad J-Q=-4v^2,\qquad u+Q-1=1,
$$
$$
M=\ell(2u-\ell Q)-u^2=v(4v^2+3v+1).
$$
因此本图允许剥除的纯 $v$ 原单位只有程序显名列出的
$$
v,\quad v-1,\quad v+1,\quad 2v+1,\quad 3v+1,\quad 4v^2+3v+1.
$$
本次不倒置任何新的消元主元、范数或参数首项。

## 3. 新十五阶 QQ 原结式

代入 $u=1+v,\ Q=1-v$ 后，P6 的双次数为 $(40,6)$，247 项；P9 为 $(78,9)$，745 项。逐系数整除并乘回，仅剥去
$$
P_6\text{ 的 }v^2(v-1)^5,\qquad
P_9\text{ 的 }v^2(v-1)^8,
$$
得到同点原必要式
$$
C_6(v,\lambda)=0,\qquad C_9(v,\lambda)=0,
$$
其双次数、项数分别为 $(33,6),212$ 与 $(68,9),665$。没有剥除未知的 $\lambda$ 根。

完整乘回后采用 primitive 整系数输入
$$
I_6=268435456\,C_6,\qquad
I_9=729583139634020400\,C_9.
$$
两者整数 content 都为一。新计算为
$$
R(v)=\operatorname{Res}_{\lambda}^{(6,9)}(I_6,I_9).
$$
它是固定原次数 $6,9$ 的十五阶 Sylvester 行列式，实际 QQ 次数为 685，非零。

固定尺寸很关键：在某个 $v_0$ 处，即使一个或两个 $\lambda$ 首项同时退化，只要原同一点 $\lambda_0$ 是两个输入的公共有限根，原 Sylvester 线性映射的求值泛函仍给非零左核，故 $R(v_0)=0$。程序没有在各 $v_0$ 处重新按降阶次数改造行列式，因而不删除首项零纤维。

随后只作精确 QQ 整除。归一化常数吸收为某个非零有理数后，完整因子恒等式为
$$
R(v)=c\,v^{12}(v-1)^{40}(2v+1)^{40}
(4v^2+3v+1)^4 H_7(v)^6\,R_{543}(v),
\qquad c\in\mathbb Q^\times,
$$
其中 $R_{543}$ 是实际返回的首一 QQ 多项式，次数 543。所有每一步商和除数都乘回。前四类因子由原单位排除，$H_7$ 的六次幂则只在已明确分开的补图中剥除。因此
$$
H_7(v)\ne0\quad\Longrightarrow\quad R_{543}(v)=0
$$
对每个本图原解都成立，包括所有其余参数首项为零的点。

## 4. 新三十五阶模原结式与严格 Gauss 返回

令 $I_{71}$ 是对已保存完整 $C_{71,29}$ 作有理数整化并完整乘回后得到的 primitive 整系数多项式。定义真实 QQ 多项式
$$
S(v)=\operatorname{Res}_{\lambda}^{(6,29)}(I_6,I_{71}).
$$
本次没有展开它的巨大 QQ 系数，只计算其固定三十五阶行列式在素数 1009 下的约化。

选素数只检查两项：首一 $R_{543}$ 的全部系数分母在 1009 下可逆，以及两个原 $\lambda$ 次数 $6,29$ 保持。没有根据结果式 gcd 的结果挑选素数。1009 是第一个合格素数，没有跳过任何候选素数。

固定原行列式的普遍多项式身份保证返回的 $\bar S$ 确是 $S$ 的约化；实际
$$
\deg\bar S=1363.
$$
这不是声称 $\deg S=1363$，也不需要该声称。另一方面，$R_{543}$ 已在 QQ 上首一，且所有系数在 $\mathbb Z_{(1009)}$ 内，所以其约化准确保持次数 543。

程序对这两个完整模多项式作真实 xgcd，并完整乘回
$$
a(v)\,\overline{R_{543}}(v)+b(v)\,\bar S(v)=v+757
\quad\text{于 }\mathbb F_{1009}[v].
$$
实际 $\deg a=1361,\ \deg b=541$。因此模 gcd 的次数准确为一。

现在设 $H$ 是 $R_{543}$ 与 $S$ 在 QQ 上的首一 gcd。由于 $R_{543}$ 是 $\mathbb Z_{(1009)}$ 上首一多项式，其任一首一 QQ 因子都属于 $\mathbb Z_{(1009)}[v]$：各根整于该局部整环，因子系数也整，且该环整闭。因而 $H$ 在 1009 下仍首一并保持次数。以首一 $H$ 对 $S$ 作多项式除法，商和余式都在该局部整环内；QQ 中整除使余式为零。于是
$$
\bar H\mid\gcd(\overline{R_{543}},\bar S),
\qquad\deg H\le1.
$$
每个补图原解的 $v$ 都同时满足 $R_{543}(v)=S(v)=0$，所以不同 $v$ 至多一个。加上完整保留的 $H_7=0$ 的至多七个复根，得到本稿的八个主权参数界。

这一步只把实际模 gcd 用于限制已付首一 QQ 公共因子的次数，没有把 $v+757$ 直接提升为任何指定 QQ 线性因子。

## 5. 精确载荷与实际执行

新源：

[2026-11-27-unit211-Phi-zero-main-rho-head-saved-P6-P9-small-original-QQ-input-8542.py](../notes/2026-11-27-unit211-Phi-zero-main-rho-head-saved-P6-P9-small-original-QQ-input-8542.py)

- Git blob：$\,\texttt{64abfa2f9aa556e85521a8f4b0e461662cc2c1cb}\,$。
- SHA256：$\,\texttt{c3a07401f79ee4c6ff91a423509cea2dfd317d37afdbe1a04fc0625f4e519899}\,$。
- 实际 run/job：46053694010 / 140690963850。
- source commit：$\,\texttt{0298b35143bc5e99acf40ef1bb452d7002df7d77}\,$。
- 内层退出码 0；0.503922414 秒；51576 KiB。
- stdout：98173 字节；SHA256 $\,\texttt{dcd2886706f6d82c21a3555d2354426348c4acd0ebcc0c6bf66a7537e58765fc}\,$。
- 实际读取规则时间：2026-11-27 19:01:39 UTC；真实 pull 后根与课题 README blob 均未变。

完整小回执：

[2026-11-27-unit211-Phi-zero-main-rho-head-eight-weight-cover-execution-8542.json](../notes/2026-11-27-unit211-Phi-zero-main-rho-head-eight-weight-cover-execution-8542.json)

新精确输入分开保存为每件不足 100 KB 的文件：

- [C6/C9 完整特化](https://github.com/Rogerhu12/math-research-public/blob/3b9cda56dfa6a1ae9d4ca2a35fa81798a5f156c9/topics/invariant-subspace-problem/notes/2026-11-27-unit211-Phi-zero-main-rho-head-P6-P9-specialized-exact-input-8542.json)，解压原文 29985 字节，SHA256 $\,\texttt{c02499bdfd8a1108eee2ba2353011279dd1d921f12d2f863b14b4d2c633f5c20}\,$。
- [实际首一 R543](https://github.com/Rogerhu12/math-research-public/blob/3b9cda56dfa6a1ae9d4ca2a35fa81798a5f156c9/topics/invariant-subspace-problem/notes/2026-11-27-unit211-Phi-zero-main-rho-head-monic-543-weight-cover-exact-input-8542.json)，解压原文 130179 字节，SHA256 $\,\texttt{4d97fcc3b5a3c56a49298d2c268ba8496b5eb672c19e54874a7ec7f4b18e99aa}\,$。
- [新固定 S 的完整模约化](https://github.com/Rogerhu12/math-research-public/blob/3b9cda56dfa6a1ae9d4ca2a35fa81798a5f156c9/topics/invariant-subspace-problem/notes/2026-11-27-unit211-Phi-zero-main-rho-head-C6-C71-modular-projection-exact-input-8542.json)，解压原文 5444 字节，SHA256 $\,\texttt{66a4dc89f9c84ee228af2bc52646e7aa656fac5677348bcd8c1e2047bacfca3b}\,$。

原输入、全部首项零纤维和完整模乘回均属于此次已完成证明；后续精确因子识别、八个权参数的原值纤维排除另用新的输入，不作为本结论的附加重放门槛。
