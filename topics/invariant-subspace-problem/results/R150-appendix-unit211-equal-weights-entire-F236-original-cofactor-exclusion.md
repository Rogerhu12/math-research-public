# R150：一般等权整个 F236 的原六行余子式排除

会话：Astra-ISP-8542378f-20261127。日期：2026-11-27。

## 1. 范围与结论

在[完整824次QQ覆盖](R150-appendix-unit211-equal-weights-complete-824-degree-original-weight-cover.md)的全部允许权参数上，整个 $F_{236}(m)=0$ 的复纤维没有原解。结合已闭的[F243](R150-appendix-unit211-equal-weights-entire-F243-original-Gauss-exclusion.md)，此时剩余权覆盖只可能为 $m=-1/2$。

本证明换取同一原十行系统的另一组原六行子式，完整保留此前所选五行非恒数头退化的纤维。它不继续假设那个五行头可逆，也不把此前全部 NS/PS 点乘未排除 F236 的结果改写为空性。

## 2. 新的完整原六行来源

沿用[原C/D余子式](R150-appendix-unit211-equal-weights-two-original-parameter-cofactor-curves.md)的十行编号与列 $(x,y,t,y^2,yt,1)$。每行都具有相对于同一个原六式的完整 trace。

本次选择原行

$$
I=(0,1,2,3,4,7).
$$

各行分别为两条未选 cubic overlap、原 NS、原 PS，以及两条 overlap 各乘 x。取非恒数五列的五阶子式，形成六个 cofactors $c_i$。实际逐列乘回：

$$
cM_I=(0,0,0,0,0,\Delta_I).
$$

这里 $\deg_{m,Q}\Delta_I=(70,63)$。只剥去原已付单位得到必要多项式 E，满足

$$
\deg_{m,Q}E=(27,27),
$$

共512项，其FLINT字符串SHA256为

02163d611202e68671ae824eef756d27e2489d0c0835b453caecf4b905283f7b。

剥除次数为 m三次、m-1十一、Q六次、Q-1三次、P02线性因子二次、J二十五次、2m-1二次；每次除法另有完整乘回。未倒置 I 的任何原主元。因此所有当前原解都满足 E=0，即使此前五行头或此处中间主元为零。

## 3. 固定51阶投影与完整因子返回

令 C 为既有原Q次数24的cofactor。定义

$$
R_I(m)=\operatorname{Res}_Q^{(27,24)}(E,C).
$$

这是固定51阶Sylvester行列式。原解在同一有限 Q 上使 E=C=0，故必有 RI=0，包括全部首项退化点。

在 p=1009 处，源码逐项检查 E、C 系数分母可逆，并确认两个Q次数保持27、24。模结式的 m 次数为858。完整整系数 F236 的模次数保持236，精确扩展Euclid实际乘回

$$
U\overline{F}_{236}+V\overline{R}_I=1,\qquad
\deg U=857,\quad\deg V=235.
$$

由保度的局部Gauss引理，F236与RI在QQ[m]中互素。因此它们不能有同一个复根，整个 F236 原权纤维被排除。该论证覆盖所有复嵌入；不要求数值找根或假设 F236 不可约。保度Gauss的完整论证与[F243证明](R150-appendix-unit211-equal-weights-entire-F243-original-Gauss-exclusion.md)第三节相同，所用新行、结式及次数在本节明确给出。

源码先处理的行组 $(0,1,2,3,4,5)$ 也通过全部原六列乘回，但其模54阶结式为零，未提供F236排除。实际Bézout向量的三个次数是 $(857,-1,235)$，中间项恰为零；没有把这个零投影计作额外独立证据。

## 4. 实际执行

自含源：[F236的另一组原六行](../notes/2026-11-27-unit211-equal-weight-F236-other-original-row-cofactors-8542.py)。

- 实际文件SHA256：34014ec5e9dc2dd09e222f039d42db58c4e2ffc3ed5ebb8c56b966d28f8d6eac。
- 本地Python3.12.14/python-flint0.9.0，单线程。
- 开始：2026-11-27 06:08:05.869455 UTC。
- 源数学完成11.217779030秒，驱动11.361538412秒，最大子进程RSS49000KiB，exit0。
- 原源预算180秒/4GiB，驱动195秒。
- stdout21469字节，SHA256：481d8ce507e8a460a0f742ab7316fa989850cef7e2ae2ef1d770fbbae0894257。
- [小回执](../notes/2026-11-27-unit211-equal-weight-F236-other-original-row-execution-8542.json)。

所有新原cofactor、已付剥除和Bézout身份实际乘回。既有失败门不重跑；普通ISP未因这一有限分支的排除而完成。
