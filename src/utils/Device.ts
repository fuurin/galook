import IsMobile from 'ismobilejs';

export default class Device {
    private m = IsMobile();

    public isMobile() {
        return this.m.phone || this.m.tablet;
    }

    public respCls(cls: string, mobileSuf = "mobile", desktopSuf = "desktop"): string {
        return cls + "-" + (this.isMobile() ? mobileSuf : desktopSuf);
    }
}
