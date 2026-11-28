# 准确 coast 末端法向带的水平投影

**已证明的端口结论。** 取准确 R233/R232 上半段的整条出口圈 $X(t)$ 及一致外法向 $n(t)$，$t$ 是原 Γ95 的 native 圆周角。对任意 $|\tau|\le.097$ 令 $Y(t,\tau)=X(t)+\tau n(t)$，并令 $V(x,y)=(x,4y)$。全角、全偏移的定向区间计算给
$$
\det(V(Y_{xy}),Y_{t,xy})>.07439,\quad
\det(n_{xy},Y_{t,xy})>.05209,\quad Y_z-c>.05617 .
$$
因此每一固定偏移的出口圈都沿 $V$ 流的椭圆足点正向绕行一次，随偏移变化又严格横过每条固定足点的流线坐标。这个实际末端全法向带可为后缀边界匹配提供定量的定向裕量。整个环带内部的非局部 reach 另由 R259 的全点对论证支付。

准确 R137 母线形式为 $X=C+(f_0/a_\Gamma)(\Gamma-C)+w(d-kT)$，其中 $2r_0w+(1+k^2)w^2=l(2r_0+l)$、$r_0=f_0/v$。沿母线法向恒定，故 $n=T\times d$。脚本消费实际 Γ95 的全部 Fourier 项、真实速度、R137 的 $k,k_u$ 和 R232 的入口 $d,d_t$，用
$$
w_t=-kk_tw^2/(r_0+(1+k^2)w),\qquad n_t=T_t\times d+T\times d_t
$$
准确微分 $X$ 与 $Y$。每个角盒取 96-bit 有向舍入的中心 Fourier Taylor 盒，$k_t=k_u|\Gamma'|/a_\Gamma$。第一个行列式在 $\tau$ 中二次，最后两项仿射。两个半区间上取二次 Bernstein 三个系数，两个端点交叉积的对称平均给中系数。正系数下界覆盖连续区间。总计 2048 角盒。另得入口外法向与对应中央材料法向之弦距 $<.234892$，此处保留 R233 中 native 角反参差 $1.075\cdot10^{-14}$。各盖盒的实际 $U_t>.96579$。

每条固定偏移边界的水平投影从不为零，按 $\tau$ 连续同伦于原末圈，通过 R257 的原环带同伦可知绕数为一。$dq$ 对 $V$ 流足点的正角导数与 $\det(V,\cdot)$ 同号，故足点沿 $t$ 全局单调。在该固定足点下，$Y_\tau+Y_t(dt/d\tau)$ 的水平分量沿 $V$，系数为 $\det(n_{xy},Y_{t,xy})/\det(V,Y_{t,xy})>0$。因而这条法向带的水平投影在两个法向端圈之间单射，给实际端口图。它本身不检查该投影和任一给定真实后缀的交会。

从课题根运行。$W$ 指原 R233/R232 两份 master 的可重生目录。

```sh
python3 scripts/2ecf-polar-accurate-tube-rim.py --scripts scripts \
  --ramp "$W/gap105-prefix-ramp-master.npz" --coast "$W/gap105-prefix-coast-master.npz" \
  --cells 2048 --offset-splits 2 --output "$W/polar-tube-rim-2048.json"
```

入口 SHA256 为 e88b8b739ae271f1d0909bbbfb81a8e2988ce5776fd6f65dc83965d483c6d8a4。整数内核和 Fourier 内核 SHA 分别为 6bc46eeeb91bb979c19c2167250ced2a8362ae92b8f8b53eacd8595408e2af57 和 0cfe24c3be23e90986345119bac15c65a018aeaa9ba909318b9bbcb4d06ddc90。实际完整报告 SHA 为 f39dbd82b87f0fac224868473c55afa9cd0ea1d5541b9d745f2215bfc9148a17，stdout 为 0e9da5ce5732dc738e62b6e9018ff5180844ac6be1dc212c44f8a98db5e7159d，外部回执为 4f83d51c70f884c722aad827b168e463ba57d62c1bfa4e40790a263495f727cf。实际返回 0，43.859437 秒，峰值 27288 KiB。报告同时保存两个完整 master SHA 与全行流 SHA。
