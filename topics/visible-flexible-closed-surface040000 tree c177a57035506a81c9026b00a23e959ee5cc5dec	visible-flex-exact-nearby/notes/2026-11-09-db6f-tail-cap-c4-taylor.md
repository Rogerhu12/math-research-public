# 跨 cap 边界的四阶 Taylor 背景包

状态：**下述条件引理有完整证明；实现与 pilot 待独立审查。** 只改变同一冻结背景的区间求值方法，不改变物理度量、有限尾图或原函数。对实际 metric 的新上界仍由连续后端另算。

作者：`/root/tail_theory`，2026-11-09。

## 1. 两个接缝的精确四阶匹配

在单个 source profile 内，令 $R(x)$ 为未 cap 的 $\log w$，$C(x)$ 为 cap 的对数，$L>0$ 为固定 transition 参数。这里 $R,C$ 在整个 profile 上光滑；source 的 shape、恢复权重以及 cap 对数插值都是有限光滑表达式。设

$$
t=\frac{R-C+L}{2L},\qquad
J(t)=t^5\left(7-14t+10t^2-\frac52t^3\right).
$$

cap 对数函数为

$$
\ell(x)=
\begin{cases}
R(x),&t\le0,\\
C(x)-L+2L(t-J(t)),&0\le t\le1,\\
C(x),&t\ge1.
\end{cases}
$$

记中支为 $\ell_m$。两个精确多项式恒等式给出

$$
\ell_m-R=-2L\,t^5\left(7-14t+10t^2-\frac52t^3\right),
\tag{1}
$$

$$
\ell_m-C=-L(1-t)^5(1+3t+5t^2+5t^3).
\tag{2}
$$

式 (2) 可直接展开；其等价形式为

$$
1-2(t-J(t))=(1-t)^5(1+3t+5t^2+5t^3).
$$

由五重零点，三个分支在各接缝处的 0 至 4 阶 $t$ 导数一致。把 $t=t(x)$ 代回并反复使用链式法则，0 至 4 阶 $x$ 导数也一致，无需假设 $t'(x)\ne0$。因而 $\ell$ 是 $C^4$。恢复段 raw0/segment7 只将它替换为 $S R+(1-S)\ell$，其中 $S$ 是光滑多项式；这一操作保留 $C^4$。最后 $w=\exp\ell$ 仍为 $C^4$。

这里不声称 $w$ 跨 cap 是 $C^5$ 或解析函数，也不声称包含 $|w_x|$ 的径向速度分解项 $A$ 是 $C^4$。使用的只有每个固定 profile 内的 source 函数 $w(x)$。

## 2. 已有 source hull 包含每点四阶导数

`db6f_tail_interval_source_stable.py` 在完全落在一个 cap 分支的盒上执行该分支的 normalized Jet 运算。区间运算给每个 $k$ 的系数一个包，包含该分支的 $w^{(k)}(x)/k!$。

跨 cap 的盒上，代码对所有可能分支作 Jet 的逐系数 hull。中支把 $t$ 的常数项与 $[0,1]$ 相交；更高 jet 项仍保留整个输入盒的导数范围。在真实属于中支的每一点，真实 $t$ 位于该交集，其各阶导数也在保留的范围中。因此用这些区间作链式法则仍包住该点的各阶中支导数。低支和高支随后分别加入 hull，不会遗漏其相应子集。

同理，source 对 smoothstep 常数项的单调范围约束、cap 导数正因子式以及 $d\in[0,1]$ 的交集，只是独立已证的范围收紧。常数 cap 的精确替换使用 $\exp(\log c)=c$ 这一实数恒等式，属于同一个真实背景。

所以对于跨 cap 的整个 source 区间 $X$，最终的 `w.c[k]` 包含每一点的真实 normalized 导数，$0\le k\le4$。接缝点的导数由第 1 节的四阶匹配唯一确定；任一相邻分支给出的值都等于该值，因此 hull 在接缝也合法。

`validB=false` 表示不能将整个盒当成一个解析分支，不表示上述四阶逐点导数包失效。新方法仅在这一明确区分下越过旧解析 flag。

## 3. 四阶余项与物理半径转移

任选二进中心 $c\in X=[x_0,x_1]$。记 $P_k$ 为 source 在 $c$ 的 normalized 导数包，$Q_p$ 为整个 $X$ 上的 normalized 第 $p$ 阶导数包，其中 $p=4$，或用户原工作阶数更小时的 $p=2$。设

$$
h=\max(|x_0-c|,|x_1-c|).
$$

由于 $w\in C^p(X)$，Taylor 积分余项给出

$$
w(x)\in\sum_{k=0}^{p-1}P_k(x-c)^k
       +[-\|Q_p\|_\infty h^p,\|Q_p\|_\infty h^p],
\qquad x\in X.
\tag{3}
$$

注意 Jet 系数已经除以 $p!$；式 (3) 的余项无需再乘或除一个阶乘。对于 $x<c$，对积分方向取绝对值给出同一个界。

原已审供应器用四个有序 Bezier 控制点构造近似反解多项式 $x_{\rm app}(\tau)$，$0\le\tau\le1$，因而它的值严格留在 $[x_0,x_1]$。将该多项式代入 (3)，通过区间多项式合成得到 source 值的合法多项式包。

原函数证书另外供应

$$
|r(x_{\rm app}(\tau))-r_{\rm linear}(\tau)|\le\delta_r.
$$

已证背景 $|w_r|<24$ 因而给真实物理半径上的附加误差 $24\delta_r$。这一步与旧供应器完全相同，也不借助 source $r$ 的高阶可微性。超过输出次数的所有系数仍按已审向外 $\ell^1$ 和加入余项。于是整个组合仍包住同一个 $w(r_{\rm linear}(\tau))$。

跨 profile 边界时，近似多项式只在其选定的合法 source profile 内取值；原有全域 Lipschitz 径向转移仍负责它与真实物理盒的距离。没有把某个 profile 的形式导数直接当成另一个 profile 的物理导数。

## 4. 实现差异与可复跑 pilot

新文件为 `scripts/db6f-tail-background-packet-c4.py`，SHA256：

```text
2c8e3c30cd7a23ee2d4c74fca9833b3454085889a28ac5fcf044029b66a4bdf3
```

它由已审总宽判据版本 `db6f-tail-background-packet-totalwidth.py` 派生。旧跨 cap 分支直接返回 degree-0 值域 hull；新版本在该处令 `order=min(order,4)`，然后继续原有 Taylor/合成/余项逻辑。另增加跨 cap 调用计数和作用域说明。其它包含性核心、强锚检查、$w_r$ 分支范围、参数/hash 绑定、物理覆盖、输出压缩均保持原文。

pilot 选取此前较难的 raw0 原网格 spans `[4568,4572)`，只支付 $w$ 的新精度；`wr-width=1e300` 是工作阈值，不丢弃任何实际 $w_r$ 区间。旧图的曲率证书另行保留。运行如下：

```bash
python scripts/db6f-tail-background-packet-c4.py \
  --manifest notes/2026-11-09-db6f-tail-int2-flat17-m8-q10-n8-s32-manifest.json \
  --primitive notes/2026-11-09-db6f-tail-background-primitive-stable-depth4.json.gz \
  --calibrations notes/2026-11-09-db6f-tail-finite-source-calibrations.json \
  --out-prefix notes/2026-11-09-db6f-tail-background-c4-pilot-raw0 \
  --span-start 4568 --span-stop 4572 \
  --w-width 1e-9 --wr-width 1e300 --radial-residual 1e-8 --max-depth 10
```

运行输出与独审另行记录，不以工作宽度或 `finished=true` 代替实际连续 metric 后端。此方法也不支付源 ODE、角频截断、真实无限非线性尾存在或完整 C² Cauchy 极限。
