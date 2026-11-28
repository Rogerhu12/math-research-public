# 正材料长度 HF 强场的 72 个实际前端曲面

**有限数值试验。** 取[完整 HF 双钟母场](2026-11-28-2ecf-strong-hf-two-material-clocks-on-new-metric.md)，$g$、相位机制和准确两端固定。在真物理材料坐标 $s$ 中从 Γ95 端口向前取 $d=s-b$；对 $0\le d\le R$ 定义实际曲面
$$X_*(s,u)=X(s,u)+\lambda w(d/R)[Q(d,u)-X(s,u)],\qquad
w(t)=(1-t)^3(1+3t+6t^2).$$
带外使用原位置。$w$ 在右端两阶消失，各 $Q$ 与母场在左端有共同两 jet。$X_*$ 的 $ss,su,uu$ 直接按乘积法重算。每个材料角分别从准确 Γ95 函数求 $P,V,A$ 和各自前两角导数；曲面上的 $g$ 与两个 clock 保持冻结。

第一族是 $Q=P+dV+d^2A/2$。其余三族以 $P+\int_0^d T(v,u)dv$ 定义，$K=|A|^2$，
$$T(v,u)=\left(\sum_{k=0}^{13}\frac{(-K\ell^2)^k}{(2k)!}\right)V
+\ell\left(\sum_{k=0}^{13}\frac{(-K\ell^2)^k}{(2k+1)!}\right)A.$$
取 $\ell=v$ 或 $\ell=t_0(1-e^{-v/t_0})$、$t_0=.035,.09$；按 24 点 Gauss 求位置积分，径向一、二导直接由被积函及其导数求取。这里的计算没有声称积分误差的区间证书。$R=.018,.035,.065,.11,.18,.26$，$\lambda=1,.65,.35$，共 72 个真实带角曲面，加恒等母场。每张 G10 对改变处与不变补集分开重算原 14 行再合并，仍为原 4291840 行。

在允许 G10 的 metric 峰增大至原值的 1.05 倍时，72 项均未取得比恒等母场更低的曲率峰。若只按 G10 曲率挑选，取到 $R=.11$、二阶多项式、$\lambda=.35$，曲率从 28.91921607 降至 22.99359102。后者最坏点移出前端，位于 $x=.5204798390$、$u=1.832595715$。新 G10 metric 为 .1485422119，原 14 行成本 .05330318458。真实独立 G11 metric .1498293802、曲率 23.04436845、held .6582741965；恒等母场 G11 为 .1083746600、28.77930742、.6582741965。两种物理改进方向的取舍清楚；没有新整闭 reach 或等距结论。

在上引记录的 hfargs 环境运行：

```bash
python "$SCRIPTS/2ecf-strong-hf-new-clock-front-curves.py" "${hfargs[@]}" --diagonal clock-hf-diagonal-d006.json --warp clock-hf-two-material-spectral.json --windows .018 .035 .065 .11 .18 .26 --families quadratic 0 .035 .09 --scales 1 .65 .35 --output clock-hf-new-front-families.json
```

73 个选前物理观察和选后才使用的独立观察完整回执 SHA-256 为 `b51f8dae9e64f3145a10efc92118137b7713708413709eaf25c7a0cadeb0ca95`。真实曲面以三元参数、已标识母场、准确端口及入口源码重生，无需保存各曲面大数组。
